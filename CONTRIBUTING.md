# Contributing Guide

For now, this is a personal project and I don't have any plans to support or
publish it. That said, pull requests are accepted and I might change my mind
if anybody else finds this project useful.

## Getting started with local development

These instructions assume that [Python 3](https://docs.python.org/3/) is
installed in your system and available in the shell's command search path as
`python3`.

Once you have cloned this repository, create and activate a temporary virtual
environment, and then install the required dependencies as follows:

```
python3 -m venv .venv
. ./.venv/bin/activate
pip install -r requirements.txt
```

You should now be able to start Python via `python -i .pythonrc` to explore this
package and its documentation interactively.

## Running unit and integration tests locally

Ensure that the temporary virtual environment created for local development is
active, and then execute the command `python -m unittest`.
