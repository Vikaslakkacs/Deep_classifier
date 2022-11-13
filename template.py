import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format= "[%(asctime)s] %(message)s:")
package_name='deepClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trails.ipynb"
]

##Create files
for filepath in list_of_files:
    filepath= Path(filepath)
    ##Split directory and file path
    filedir, filename= os.path.split(filepath)
    ## If only file directory is present then only create directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    ##If file doesn't exists or file size is noting then create file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass # Create empty file
            logging.info(f"Creating file: {filename} in path: {filedir}")
    else:
        logging.info(f"file: {filename} already exists")

