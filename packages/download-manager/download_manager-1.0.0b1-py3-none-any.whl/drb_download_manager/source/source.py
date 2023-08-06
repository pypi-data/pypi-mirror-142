from abc import ABC, abstractmethod
from drb import DrbNode
from drb_impl_odata import ODataQueryPredicate
from requests.auth import AuthBase
import requests
from typing import List
from tenacity import retry, stop_after_delay, stop_after_attempt, wait_fixed
from drb_impl_odata.odata_nodes import ODataServiceNode, OdataServiceType


class ODataDownloadRequestException(Exception):
    pass


class Source(ABC):
    @abstractmethod
    def list(self, filter: str, top: int, skip: int) -> List[DrbNode]:
        """The abstract method aims to return the list of DRB Node retrieved
        from the service.

        :param filter: data filter in the service filter systel syntax.
        :param top: number of element to return.
        :param skip: number of element to skip.
        :return: the generator of retrieved nodes
        """
        raise NotImplementedError

    @abstractmethod
    def content_size(self, node: DrbNode) -> int:
        '''
        Use service to retrieve node size.
        :param node: the node to retrieve the content size
        :return: the size of the content.
        '''
        raise NotImplementedError


def _join_with_none(sep: str, join_list: List[str]):
    """
    Manage join string canceling None element strings:
      ' and '.join(['A','B'])
      return 'A and B'

      ' and '.join(['A','B', None])
      return 'A and B'

      ' and '.join(['A', None])
      return 'A'

    :param sep:
    :param join_list:
    :return:
    """
    lst = [x for x in join_list if x is not None]
    return sep.join(lst)


class OdataSource(Source):
    """
    ODataSource Class is the implementation of DrbNode retrieval from an OData
    service.
    """
    def __init__(self, service: str, auth: AuthBase = None):
        self.service = service
        self.auth = auth
        self.odata_service = ODataServiceNode(self.service, auth=self.auth)

    def list(self, filter: str = None, top: int = None, skip: int = None) ->\
            List[DrbNode]:
        if filter:
            # GSS issue: all ' shall be replaced by %27
            filter = filter.replace('\'', '%27')

        _type = self.odata_service.type_service
        online_filter = None
        if _type == OdataServiceType.ONDA_DIAS and \
                (filter is None or 'offline' not in filter):
            online_filter = 'offline eq false'

        if _type in (OdataServiceType.CSC, OdataServiceType.DHUS) and \
                (filter is None or 'Online' not in filter):
            online_filter = 'Online eq true'

        if online_filter is not None:
            filter = _join_with_none(' and ', [filter, online_filter])

        return self.odata_service[
            ODataQueryPredicate(filter=filter, top=top, skip=skip)]

    def content_size(self, node: DrbNode) -> int:
        content_size = 0
        _type = self.odata_service.type_service
        if _type == OdataServiceType.DHUS:
            content_size = node.get_attribute('ContentLength')
        if _type == OdataServiceType.ONDA_DIAS:
            content_size = node.get_attribute('size')
        if _type == OdataServiceType.CSC:
            content_size = node.get_attribute('ContentLength')
        return content_size

    def get_download(self):
        '''
        This method has been added temporary to manage ODATA.Http Download
        that are not able to manage range http headers.
        :return: an initialized download class
        '''
        return Download(self.odata_service)


class Download:
    def __init__(self, svc: ODataServiceNode):
        self.svc = svc

    @retry(stop=(stop_after_delay(120) | stop_after_attempt(5)),
           wait=wait_fixed(15))
    def read(self, node: DrbNode, offset, length):
        headers = None
        if offset is not None:
            if length is not None:
                headers = {"range": f"bytes={offset}-{offset+length}"}
            else:
                headers = {"range": f"bytes={offset}-"}
        response = requests.get(node.path.name + "/$value", stream=True,
                                auth=self.svc.get_auth(), headers=headers)
        if response.status_code >= 300:
            raise ODataDownloadRequestException(
                f"ERROR {response.status_code} : {response.reason} " +
                f"Request : " + response.request.url)

        return response.content
