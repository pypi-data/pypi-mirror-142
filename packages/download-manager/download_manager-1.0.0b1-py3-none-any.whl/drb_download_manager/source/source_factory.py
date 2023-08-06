from requests.auth import AuthBase
from drb_download_manager.source.source import OdataSource


class SourceFactory:
    @staticmethod
    def create_source(service: str, auth: AuthBase):
        """
        Current implementation only manage OData - Next shall use drb resolver.
        :param service:
        :param auth:
        :return:
        """
        return OdataSource(service=service, auth=auth)
