# PythonBotNovice

## Create enviroment

https://qiita.com/teri_man95/items/b15fd8f1964612331be2

check python versions

```
pyenv versions
```

change python version (local)

```
pyenv local 3.12.0
```

install virtualenv

```
pip install virtualenv
```

create virtual env

```
pyenv virtualenv 3.12.0 venv
```

activate

```
. ./venv/bin/activate
```

deactivate

```
pyenv deactivate
```

## Install

install library

```
pip install -r requirements.txt
```

add library

```
pip install requests
```

write requirements.txt

```
pip freeze > requirements.txt
```

## Execution

test

```
pytest -s tests/test_hyperliquid_manager.py
```

execute

```
python src/main.py
```

docker

```
docker compose up --build
```
