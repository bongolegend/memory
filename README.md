# Memory
Record and query your memories with voice.

### Motivation
Imagine the ability to be reminded of what you were thinking five years ago.

# Development

### Setup
- built with python 3.12 (this is not forced by any deps to my knowledge, just starting fresh)
- create virtual env
```
python3.12 -m venv venv
```
- activate venv
```
source venv/bin/activate
```
- install pip-tools
```
pip install pip-tools
```
- install deps
```
python -m pip install -r requirements/dev.txt
python -m pip install -r requirements/prod.txt

- add new deps to `requirements/*.in`, then run this to recompile the lock files (you'll need to reinstall deps again)
```
pip-compile requirements/prod.in --output-file=requirements/prod.txt
pip-compile requirements/dev.in --output-file=requirements/dev.txt
```
