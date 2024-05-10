# Memory
Record and query your memories with voice.

### Motivation
Imagine the ability to be reminded of what you were thinking five years ago.

# Development

### Setup
- built with python 3.12 (this is not forced by any deps to my knowledge, just starting fresh)
- create virtual env

```python3.12 -m venv venv```

- activate venv

```source venv/bin/activate```

- install pip-tools

```pip install pip-tools```

- install deps
```
pip-compile requirements/prod.in --output-file=requirements/prod.txt
pip-compile requirements/dev.in --output-file=requirements/dev.txt
```
