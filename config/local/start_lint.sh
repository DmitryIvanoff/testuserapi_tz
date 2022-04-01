#!/bin/bash
set -x

mypy .
isort --check-only .
black --check .
