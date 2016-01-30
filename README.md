# vOzForums Images Downloader

### How to use

* Clone this repository
* Install Python virtualenv
* Run command ``virtualenv voz-imgs-dowloader``
* Change directory into this repository folder
* Active virtual environment mode by command ``source bin/active``
* Run command ``python setup.py develop`` to install some packages dependencies
* Chmod ``voz-downloader`` to executable by command ``chmod +x voz-downloader``
* Run program with -h or --help to see instruction

### Command arguments
* id: Thread id
* start: Start page
* end: End page
* dir: Target directory to save downloaded files


### Example

``./voz-downloader -h``

``./voz-downloader 2065093 1 2 ~/Desktop/imgs/``
