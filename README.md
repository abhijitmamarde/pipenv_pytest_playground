# Sample test project for pipenv usage

install at user level
(windows)

```
py -m pip install --user pipenv
```

The main commands are:
`install`, `uninstall`, and `lock`, which generates a `Pipfile.lock`. 

These are intended to replace:

`$ pip install` usage, as well as manual virtualenv management (to activate a virtualenv, run `$ pipenv shell`).

```bash
# create new env using Python
# creates Pipfile, with required Python version,
# without any package dependencies
pipenv --three

# or can directly install required packages
# creates Pipfile and Pipfile.lock
# pipfile has only the mentioned packages
# whereas, lock file has all required dependencies, similar to - pip freeze
pipenv install requests loguru baker

# to install specific versions
pipenv install requests~=1.2

# if there is Pipfile in current dir
# or if there is only requirements.txt in dir, uses that
pipenv install

# to install from specific requriement file:
pipenv install -r path/to/requirements.txt


# install packages exactly like in `Pipfile.lock`
pipenv sync

# to verify your `Pipfile.lock` is up-to-date with dependencies specified in the `Pipfile`, without installing
pipenv verify

# find/check whats updated in package versions
pipenv update --outdated

# to update all packages versions
pipenv update

# or, update specific packages
pipenv update requests

# open specific package
set EDITOR=code
pipenv open baker
```

If a `.env` file is present in your project, `$ pipenv shell` and `$ pipenv run` automatically loads it

```bash
# touch .env
HELLO=WORLD
```


### Commands

1. Check dependency graph

```bash
D:\> pipenv graph
Baker==1.3
loguru==0.6.0
  - colorama [required: >=0.3.4, installed: 0.4.5]
  - win32-setctime [required: >=1.0.0, installed: 1.1.0]
requests==2.28.1
  - certifi [required: >=2017.4.17, installed: 2022.9.24]
  - charset-normalizer [required: >=2,<3, installed: 2.1.1]
  - idna [required: >=2.5,<4, installed: 3.4]
  - urllib3 [required: >=1.21.1,<1.27, installed: 1.26.12]
```

2. Activate virtualenv

-   `pipenv shell` will spawn a shell with the virtualenv activated. 
- This shell can be deactivated by using `exit`.
- `run` will run a given command from the virtualenv, with any arguments forwarded (e.g. `$ pipenv run python` or `$ pipenv run pip freeze`).

```bash
D:\> pipenv run pip freeze
Baker==1.3
certifi==2022.9.24
charset-normalizer==2.1.1
colorama==0.4.5
idna==3.4
loguru==0.6.0
requests==2.28.1
urllib3==1.26.12
win32-setctime==1.1.0
```

3. Editiable dependencies

```bash
# install current path '.' as editable, dev dependency
pipenv install --dev -e .
```

4. Custom Script Shortcuts

in your Pipfile add:
```bash
myscript = "python -c \"print('I am a silly example, no one would need to do this')\""
```

then you can run the custom script as:

```bash
pipenv run myscript

# to show all available scripts
pipenv scripts
```
