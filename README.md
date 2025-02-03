# Python version

A project to try out new features of the latest versions of Python.

## Py3.10

1. Install python

```
uv python install 3.10
```

2. List python versions

```
uv python list
```

3. Run the python interpreter

```
uv run -p 3.10 python -c "import sys; print(sys.version)"
```

### Project for Python 3.10

1. Create a project

```
uv init py3.10 --name py3.10 -p 3.10
```

2. Change to the project directory

```
cd py3.10
```

3. Setup the virtual env directory

```
export UV_PROJECT_ENVIRONMENT=~/.cache/venv/$(basename $(pwd))
```

4. Create a virtual env

```
uv venv
```

5. Add the requests library in the project dependencies

```
uv add requests
```

6. Run the project

```
uv run python hello.py
```

7. Change to the parent directory

```
cd ..
```

8. Run the code from the parent directory

```
uv run --directory py3.10 python hello.py
```

## Py3.11

1. Install python

```
uv python install 3.11
```

2. List python versions

```
uv python list
```

3. Run the python interpreter

```
uv run -p 3.11 python -c "import sys; print(sys.version)"
```

### Project for Python 3.11

1. Create a project

```
uv init py3.11 --name py3.11 -p 3.11
```

2. Change to the project directory

```
cd py3.11
```

3. Setup the virtual env directory

```
export UV_PROJECT_ENVIRONMENT=~/.cache/venv/$(basename $(pwd))
```

4. Create a virtual env

```
uv venv
```

5. Run the project

```
uv run python py3.11.py
```

6. Change to the parent directory

```
cd ..
```

7. Run the code from the parent directory

```
uv run --directory py3.11 python py3.11.py
```

## Py3.12

1. Run the python interpreter

```
uv run -p 3.12 python -c "import sys; print(sys.version)"
```

### Project for Python 3.12

1. Create a project

```
uv init py3.12 --name py3.12 -p 3.12
```

2. Change to the project directory

```
cd py3.12
```

3. Setup the virtual env directory

```
export UV_PROJECT_ENVIRONMENT=~/.cache/venv/$(basename $(pwd))
```

4. Create a virtual env

```
uv venv
```

5. Run the python program

```
uv run py3.12.py
```

## Py3.13

1. Run the python interpreter

```
uv run -p 3.13 python -c "import sys; print(sys.version)"
```

### Project for Python 3.13

1. Create a project

```
uv init py3.13 --name py3.13 -p 3.13
```

2. Change to the project directory

```
cd py3.13
```

3. Setup the virtual env directory

```
export UV_PROJECT_ENVIRONMENT=~/.cache/venv/$(basename $(pwd))
```

4. Create a virtual env

```
uv venv
```

5. Run the python program

```
uv run py3.13.py
```
