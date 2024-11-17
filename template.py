import os
import logging 
from pathlib import Path

logging.basicConfig(level=logging.INFO)

proj = 'chicken'
folds = [
    ".github/workflows/.gitkeep",
    f"src/{proj}/__init__.py",
    f"src/{proj}/components/__init__.py",
    f"src/{proj}/utils/__init__.py",
    f"src/{proj}/config/__init__.py",
    f"src/{proj}/pipeline/__init__.py",
    f"src/{proj}/config/configuration.py",
    'config/config.yaml',
    'dvc.yaml',
    'req.txt',
    'setup.py',
    'params.yaml',
    'research/trails.ipynb'
]

for file in folds:
    file = Path(file)
    dir, name = os.path.split(file)

    if dir:
        os.makedirs(dir, exist_ok=True)
        logging.info(f'creaating the file {name} in {dir}')
        
    if(not os.path.exists(file) or (os.path.getsize(file) == 0)):
        with open(file, 'w') as f:
            pass
            logging.info(f'creating a file empty {file}')
    
    else:
        logging.info(f'{file} already exists')

