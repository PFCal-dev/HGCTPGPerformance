#! /usr/bin/env bash

# setup Python 2.7 and ROOT 6
source /opt/rh/python27/enable
source /afs/cern.ch/sw/lcg/external/gcc/4.9/x86_64-slc6-gcc49-opt/setup.sh
source /afs/cern.ch/sw/lcg/app/releases/ROOT/6.06.08/x86_64-slc6-gcc49-opt/root/bin/thisroot.sh

# Install virtualenvwrapper package if not already installed
if [ ! -f ~/.local/bin/virtualenvwrapper.sh ]; then
  # deleting cached packages to force download
  rm -rf ~/.cache/pip/
  pip2.7 install --user -I virtualenvwrapper
fi

# Create virtual env and install dependencies
if [ ! -d ~/.virtualenvs/hgc_tpg/ ]; then
  mkdir -p ~/.virtualenvs/
  export WORKON_HOME=~/.virtualenvs
  export VIRTUALENVWRAPPER_PYTHON=`which python`
  export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
  source ~/.local/bin/virtualenvwrapper.sh
  mkvirtualenv hgc_tpg
  # deleting cached packages to force download
  rm -rf ~/.cache/pip/
  pip install -r requirements.txt -I --no-cache-dir
  pip install -e .
else
  export WORKON_HOME=~/.virtualenvs
  export VIRTUALENVWRAPPER_PYTHON=`which python`
  export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
  source ~/.local/bin/virtualenvwrapper.sh
  workon hgc_tpg
  # Check if all the package requirements are satisfied
  available_dep_count=$(pip freeze | grep -f requirements.txt | wc -l)
  needed_dep_count=$(cat requirements.txt | wc -l)
  if [ "$available_dep_count" != "$needed_dep_count" ]; then
    echo "Updating dependencies"
    # deleting cached packages to force download
    rm -rf ~/.cache/pip/
    pip install -r requirements.txt -I --no-cache-dir
  fi
fi
