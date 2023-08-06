import os.path
from queue import PriorityQueue

import click
from requests.auth import HTTPBasicAuth
from tqdm import tqdm

from drb_download_manager.utility import slice_file, PrioritizedItem
from drb_download_manager.source.source_factory import SourceFactory
from drb_download_manager.destination.writer import FileWriter

import drb_download_manager.source.source_download as source_util


# Uncomment to configure logs
# import logging
# FORMAT = '%(asctime)s %(filename)s %(message)s'
# logging. basicConfig(level=logging.DEBUG, format=FORMAT)


'''
TODO::
@click.option('--check-integrity', '-v', is_flag=True,
              help="Check file integrity by hashes.")
@click.option('--continue', '-c', is_flag=True,
              help="Continue downloading a partially downloaded file.")
@click.option('--max-tries', '-m', type=int, default=5,
              help="Number of tries (default: 5).")
@click.option('--retry-wait', type=int, default=15,
              help="Seconds to wait between retries (default: 15s).")
@click.option('--timeout', type=int, default=120,
              help="Connection timeout in seconds (default: 120s).")
@click.option('--quota-max-connections', type=int, default=0,
              help="Maximum of number connections. 0: unlimited (default: 0).")
@click.option('--quota-max-bandwidth', type=int, default=0,
              help="Maximum of bandwidth usage. 0: unlimited (default: 0).")
'''
tool_name = "download_manager"


@click.command(help=f"""
Manage transfer of data from internet. {tool_name} supports parallel and
partial transfers, and it is able to resume interrupted downloads.
It is able to handle all protocol supported by DRB, including OData (CSC,
DataHub and DIAS API declinations) for LTA and AIP.
It authorize limiting the connections to respect the services quota policies.
""")
@click.option('--service', '-s', type=str, help='Service to requests data',
              required=True)
@click.option('--filter', '-f', type=str, help="Filters service products.")
@click.option('--username', '-u', type=str,
              help="Service connection username.")
@click.option('--password', '-p', type=str,
              help="Service connection password.")
@click.option('--threads', '-t', type=int, default=4,
              help="Number of parallel download threads (default:4).")
@click.option('--top', '-l', type=int,
              help="Limit the number matching products (default: 10)",
              default=10)
@click.option('--output_folder', '-o', type=str, default="",
              help='The directory to store the downloaded files.')
@click.option('--quiet', '-q', is_flag=True,
              help="Silent mode: only errors are reported.")
@click.option('--chunk-size', '-c', type=int, default=4194304,
              help="The size of download chunks (default: 4194304).")
def download_file(service, threads, username, password, chunk_size,
                  filter, top, quiet, output_folder):

    source = SourceFactory.create_source(service,
                                         HTTPBasicAuth(username, password))
    nodes = source.list(filter=filter, top=top)

    queue = PriorityQueue()
    bars = {}
    total_sizes = 0

    for node in nodes:
        file_size = source.content_size(node)
        output = os.path.join(output_folder, node.name)
        writer = FileWriter(out_path=output, file_size=file_size)
        parts = slice_file(file_size, chunk_size)
        total_sizes += file_size

        if not quiet:
            bars[node.name] = tqdm(total=file_size, desc=node.name,
                                   colour='GREEN')
        for part in parts:
            queue.put(PrioritizedItem(5, {node.name: [part, node, writer,
                                                      source.get_download()]}))
    if not quiet:
        bars['Total'] = tqdm(total=total_sizes, desc='Total Download',
                             colour='RED')
    source_util.start_download(threads, queue, bars)
