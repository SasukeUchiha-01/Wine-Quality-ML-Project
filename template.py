import os
from pathlib import Path
import logging as log

log.basicConfig(level=log.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'wineQuality'

list_of_files = [
    f"src/{project_name}/__init__.py", # constructor file (need when we want to install folder as our local package)
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        log.info(f'Creating directory; {filedir} for the file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            log.info(f'Createing empty file: {filepath}')

    else:
        log.info(f'{filename} is already exists')