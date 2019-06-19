#!/bin/bash

if [ $(pyenv versions| grep -c "2.7.6" ) -eq 0 ]; then
  pyenv install 2.7.6
fi

if [ $(pyenv versions| grep -c "3.6.1" ) -eq 0 ]; then
  pyenv install 3.6.1
fi

if [ $(pyenv versions| grep -c "virtualenv1" ) -eq 0 ]; then
  pyenv virtualenv 2.7.6 virtenv-2.7.6
fi

if [ $(pyenv versions| grep -c "virtualenv1" ) -eq 0 ]; then
  pyenv virtualenv 3.6.1 virtenv-3.6.1
fi
