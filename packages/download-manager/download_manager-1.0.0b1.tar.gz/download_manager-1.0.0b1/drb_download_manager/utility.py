from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from math import ceil

from drb import DrbNode

from drb_download_manager.destination.writer import Writer
from drb_download_manager.source.source import Download

progress = dict()


@dataclass(order=True)
class PrioritizedItem:
    """
    This data class creates object to prioritize download of some files.
    The key of item dict is the name of the file and the value, a tuple with
    the first and last byte to be downloaded, followed by the input node and
    initialized writer. i.e.
    item: {
       'filename.zip': 0, 4000000, node, writer }

    Parameters:
        priority: (int)
        item: dict
    """
    priority: int
    item: dict = field(compare=False)


def slice_file(file_size: int, chunk_size=4194304):
    """
    Slices file as a list of ranges. Ranges are computed from the size of the
    file divide by the chunk size. A chunk is a minimum piece of the file to
    be transferred.

    The chunk size is default 4Mb and can be modified. Some bench shows that
    too small chunks reduces the transfer performances (could depend on the
    network MTU). Too big also could raise problem because of the memory
    usage.

    Parameters:
        file_size: (int) the file size to be transferred in byte.
        chunk_size: (int) the minimum chunk size in bytes (default 4194304).


    Return:
        A list of offset position chnuks in the input data to be transfer
        ([begin offset, end offset] in byte).
    """
    if not file_size:
        raise ValueError("Size of file is required.")

    chunk_list = []
    chunk_number = ceil(file_size / chunk_size)
    for chunk_count in range(chunk_number):
        start = chunk_count*chunk_size
        end = start + chunk_size-1
        end = end if file_size > end else file_size - 1
        chunk_list.append((start, end))

    return chunk_list


class ManagedThreadPoolExecutor(ThreadPoolExecutor):
    """
    Managed Thread Pool Executor. A subclass of ThreadPoolExecutor.
    """

    def __init__(self, max_workers):
        ThreadPoolExecutor.__init__(self, max_workers)
        self._futures = []

    def submit(self, fn, *args, **kwargs):
        future = super().submit(fn, *args, **kwargs)
        self._futures.append(future)
        return future

    def done(self):
        return all([x.done() for x in self._futures])

    def get_exceptions(self):
        excepts = []
        for x in self._futures:
            if x.exception():
                excepts.append(x.exception())
        return excepts


def update_progress_bar(handler):
    global progress

    def new_handler(children: DrbNode, start: int, stop: int,
                    filename: str, bars,
                    writer: Writer, download: Download):

        ret = handler(children, start, stop, filename, bars,
                      writer, download)

        if len(bars) > 0:
            bars[filename].update(ret)
            bars['Total'].update(ret)

        if progress.get(filename) is None:
            progress[filename] = ret
        else:
            progress[filename] += ret

        # Once all the chunk written the writer shall be finalized.
        try:
            if progress[filename] == writer.file_size:
                # logger.debug(f"Closing {filename}")
                writer.close()
        except Exception:
            # file_size not a attr of write: Only implemented for File Writed
            # TODO: Find an other method to identify the end of download.
            pass

    return new_handler
