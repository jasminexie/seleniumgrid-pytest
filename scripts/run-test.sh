#!bin/bash

# run pytest in virtualenv
poetry run pytest

# clean up
pyclean () {
    find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
}
pyclean
