docker container for libcgal-dev, and checkout and build python3 bindings. includes a python script for region growing. tested with .pts files. Usage:

Run these commands in the Dockerfile folder (adjust local paths):

```powershell
docker build -t pythonubuntu .
docker run -it -v C:\proj\docker-cgalpython\sharedir:/things pythonubuntu
```

inside the bash 

```bash
nano /things/segmentation.py
python3 /things/segmentation.py
```
