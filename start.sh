#!/bin/bash

echo 'Checking depencencies...'
# Checking if the pygame package is installed
if python3 -c 'import pkgutil; exit(not pkgutil.find_loader("pygame"))'; then
    echo 'pygame is installed.'
else
    echo 'pygame package is not found. Attempting to install pygame...'
    echo 'excuting pip3 install pygame'
    pip3 install pygame
fi

# Checking if the pyyaml package is installed
if python3 -c 'import pkgutil; exit(not pkgutil.find_loader("yaml"))'; then
    echo 'pyyaml is installed.'
else
    echo 'pyyaml package is not found. Attempting to install pyyaml...'
    echo 'excuting pip3 install pyyaml'
    pip3 install pyyaml
fi

python3 startup.py