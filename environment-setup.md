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
<hr/>

### install Poetry

```shell
>>> curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
>>> source $HOME/.poetry/env
# to run poetry when shell opens
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
# if pyenv doesn't change your current shell
>>> source "$( poetry env list --full-path | grep Activated | cut -d' ' -f1 )/bin/activate"
>>> poetry env use python
Creating virtualenv python-setup-j-Htv8gO-py3.9 in /Users/username/Library/Caches/pypoetry/virtualenvs
Using virtualenv: /Users/username/Library/Caches/pypoetry/virtualenvs/python-setup-j-Htv8gO-py3.9
```
<hr/>

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
<hr/>

### use pytest
```shell
>>> poetry run pytest
# install pytest-cov to see more coverage
>>> poetry add --dev pytest-cov
>>> poetry run pytest --cov=prac
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/username/workspace/python-setup
plugins: cov-2.12.1
collected 1 item

prac/test_prac.py .                                                                                                                                   [100%]

---------- coverage: platform darwin, python 3.9.7-final-0 -----------
Name                Stmts   Miss  Cover
---------------------------------------
prac/prac.py           11      5    55%
prac/test_prac.py       4      0   100%
---------------------------------------
TOTAL                  15      5    67%

===================================================================== 1 passed in 0.03s =====================================================================
```
<hr/>

### pre-commit (for git user)
pre-commit is a tool to run pre-check on every git commit

install
```shell
>>> poetry add pre-commit --dev
# to create sample file for pre-commit use.
>>> pre-commit sample-config > .pre-commit-config.yaml
>>> pre-commit run --all-files
```

<hr/>

### flake8 (link: [flake8](https://flake8.pycqa.org/en/latest/))

```shell
>>> poetry run flake8 .
./prac/prac.py:3:1: E302 expected 2 blank lines, found 1
./prac/prac.py:7:1: E302 expected 2 blank lines, found 1
./prac/prac.py:9:36: E231 missing whitespace after ','
./prac/prac.py:13:1: E302 expected 2 blank lines, found 1
./prac/test_prac.py:3:1: E302 expected 2 blank lines, found 1
```


<hr/>

### Add `Black` as a formatter
```shell
>>> poetry add --dev black --allow-prereleases
```

and.... add the following sections to `pyproject.toml`

```toml
[tool.black]
line-length = 79
target-version = ['py38']
include = '\.pyi?$'
exclude = '''

(
  /(
      \.eggs         # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
  )/
  | foo.py           # also separately exclude a file named foo.py in
                     # the root of the project
)
'''
```

To run
```shell
>>> black .
All done! ✨ 🍰 ✨
2 files left unchanged.
>>> pre-commit run --all-files
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...............................................................Passed
Check for added large files..............................................Passed
flake8...................................................................Passed
black....................................................................Passed
```

Add Black to git hooks

```yaml
-   repo: https://github.com/psf/black
    rev: 20.8b1
    hooks:
      - id: black
```

### Install mypy as a type hinter
To install
```shell
poetry add --dev mypy
```
To run
```shell
# to all directories
mypy .
```

Create `setup.cfg` file and add following lines
```buildoutcfg
[mypy]
follow_imports = silent
strict_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
disallow_any_generics = True
check_untyped_defs = True
no_implicit_reexport = True
disallow_untyped_defs = True
ignore_missing_imports = True
```
In case, you want to disable mypy on tests,

```buildoutcfg
[mypy-tests.*]
ignore_errors = True
```
Also, in case, you want to use mypy with Pydantic modules,
```buildoutcfg
[mypy]
plugins = pydantic.mypy

follow_imports = silent
strict_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
disallow_any_generics = True
check_untyped_defs = True
no_implicit_reexport = True
disallow_untyped_defs = True
ignore_missing_imports = True

[pydantic-mypy]
init_forbid_extra = True
init_typed = True
warn_required_dynamic_aliases = True
warn_untyped_fields = True
```

If everything works well, you may see these
```shell
>>> prac/test_prac.py:4: error: Function is missing a return type annotation
prac/test_prac.py:4: note: Use "-> None" if function does not return a value
Found 1 error in 1 file (checked 2 source files)
```
