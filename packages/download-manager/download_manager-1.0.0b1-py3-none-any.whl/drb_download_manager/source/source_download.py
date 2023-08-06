import logging
from queue import PriorityQueue
from drb_download_manager.utility import ManagedThreadPoolExecutor, \
    update_progress_bar
from drb import DrbNode
from drb_download_manager.destination.writer import Writer
from drb_download_manager.source.source import Download


class DownloadRequestException(Exception):
    pass


logger = logging.getLogger("download")


@update_progress_bar
def handler(children: DrbNode, start: int, stop: int, filename: str, bars,
            writer: Writer, download: Download):
    logger.debug(f"Handler started for {filename}[{start}-{stop}]")

    buff = download.read(children, start, stop - start)

    # open the file and write the content of the download
    writer.write(buff, start)
    return len(buff)


def start_download(number_of_threads: int, queue: PriorityQueue, bars):
    future_download = set()
    with ManagedThreadPoolExecutor(max_workers=number_of_threads) as executor:
        while not queue.empty():
            item = queue.get()
            for item_name in item.item:
                (start, stop), node, writer, download = item.item[item_name]
                future_download.add(executor.submit(
                    handler, children=node, start=start, stop=stop,
                    filename=item_name, bars=bars, writer=writer,
                    download=download))

    '''
    Uncomment to see handler exceptions
    for result in future_download:
        # This will cause the exception to be raised (but only the first one)
        print(result.result())
    '''

    for bar in bars.values():
        bar.close()
