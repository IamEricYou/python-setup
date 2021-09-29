### install pyenv

`brew install pyenv`

```shell
>>> pyenv versions
* system (set by /Users/"username"/.pyenv/version)
  3.9.7

# To see all available versions
>>> pyenv install --list | grep " 3/. "
...
  3.8.8
  3.8.9
  3.8.10
  3.8.11
  3.8.12
  3.9.0
  3.9-dev
...
```

### install Poetry

```shell
>>> curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
>>> source $HOME/.poetry/env
# to run poertry when shell opens
>>> export PATH="$HOME/.poetry/bin:$PATH"
```

### start Poetry
```shell
>>> poetry new project
# or if you want to init on your existed project
>>> poetry init
>>> pyenv local 3.9.7
>>> pyenv versions
  system
* 3.9.7 (set by /Users/username/workspace/python-setup/.python-version)
>>> python -V
Python 3.9.7

# if pyenv local doesn't work for you, try this first
>>> eval "$(pyenv init --path)"
>>> poetry env use python
Creating virtualenv python-setup-j-Htv8gO-py3.9 in /Users/username/Library/Caches/pypoetry/virtualenvs
Using virtualenv: /Users/username/Library/Caches/pypoetry/virtualenvs/python-setup-j-Htv8gO-py3.9
```

### use Poetry

```shell
>>> poetry add tqdm
# install all packages and dependencies
>>> poetry install
# update all packages and dependencies
>>> poetry update
# and start the shell
>>> poetry shell
Spawning shell within /Users/username/Library/Caches/pypoetry/virtualenvs/python-setup-j-Htv8gO-py3.9
```

