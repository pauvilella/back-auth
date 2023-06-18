<h1 align="center"> back-auth </h1> <br>

<p align="center">
Backend service with authentication.
</p>


## Table of Contents
- [Table of Contents](#table-of-contents)
- [Setup](#setup)
  - [Requirements](#requirements)
  - [One time configuration](#one-time-configuration)
  - [Build](#build)
  - [Start](#start)
- [Local development](#local-development)
  - [Debugging](#debugging)

## Setup

### Requirements

Check that you have installed:
* Poetry
* Pre-commit

### One time configuration

In a terminal inside this project directory:

Configure poetry (if it not already exists, Poetry will create a new virtual enviornment in this directory too, in a `.venv` folder):
```bash
poetry install
```
And once installed all the libraries with poetry, remember to configiure pre-commit and autoupdate to set the versions of the libraries to the required by pre-commit:
```bash
pre-commit install
pre-commit autoupdate
```

### Build

```bash
docker compose build
```

### Start
```bash
docker compose up
```

## Local development

### Debugging
```bash
DEBUGPY=True docker compose up
```
Once the service has started, open the debug view on vscode:

<b>command + alt + D</b>
