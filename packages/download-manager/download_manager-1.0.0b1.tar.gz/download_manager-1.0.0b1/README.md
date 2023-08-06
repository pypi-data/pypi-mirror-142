# download-manager
Download Manager is a single python tool dedicated to help to download 
products from LTA and AIP.

## Download manager features
The tool has been implemented with the objective to implements the following
features:

- Manage download in a configurable local folder,
- Manage partial downloads and recovery downloads,
- Manage parallelized downloads
- Manage bulk download
- Management of connections error/retry
- Monitoring of downloads (bandwidth/progress) and errors
- Run in command line (GUI is a nice to have)
- Support of multiple sources
- Manage checksum validation of downloads
- Local storage management (identification of incomplete downloads to be resume, evictions...)

- Manage/anticipate quota limitation:
  - bandwidth limitation
  - parallel transfers number
  - transfer volume per time
  ..
- Download list issued from an OData filter
- Manage OData endpoint notifications/action when new product matching filter 
is up to allow performing routine downloads.

## Install the download manager

Download the project from git, and install the requirements.

```
pip install -r requirements.txt
```

## Getting started

Download one product, with one thread:

```
download_manager.py --service odata://service.com/ -t 1 -u user -p password -l 1
```

Download 10 products:

```
download_manager.py --service odata://service.com/ -u user -p password -l 10
```

Use the silent option:

```
download_manager.py --service odata://service.com/ -u user -p password --silent
```


## Limitation

For now only odata implementation is available, quota still not supported.

The error management is implemented but cannot be parametrized in command line.

Offline product are not yet supoorted.