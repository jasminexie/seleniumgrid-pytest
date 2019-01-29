#!bin/bash

set -e

# install pip
if ! [ -x "$(command -v pip)" ]; then
  echo '----------Installing pip----------' >&2 
  sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  sudo python get-pip.py
fi

# install poetry
echo "----------Installing Poetry----------"
sudo curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
source $HOME/.poetry/env

# install dependencies
poetry install
