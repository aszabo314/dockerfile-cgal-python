docker container for libcgal-dev, and checkout and build python3 bindings. includes a python script for region growing. works with .pts files. Usage:

Run these commands in the Dockerfile folder (adjust local paths):

`docker build -t pythonubuntu .`
`docker run -it -v C:\proj\docker-cgalpython\sharedir:/things pythonubuntu`

inside the bash 

`nano /things/segmentation.py`
`python3 /things/segmentation.py`