#!/bin/bash

# Copyright OpenSearch Contributors.
# SPDX-License-Identifier: Apache-2.0

set -e

if [ -z "$1" ]; then (echo "syntax: run.sh [workflow.py]"; exit -1); fi
command -v python3 >/dev/null 2>&1 || (echo "missing python3"; exit -1)
command -v pip >/dev/null 2>&1 || (echo "missing python3-pip"; exit -1)
command -v pipenv >/dev/null 2>&1 || (echo "missing pipenv"; exit -1)

DIR="$(dirname "$0")"

echo "Installing dependencies in $DIR ..."
export PIPENV_PIPFILE="$DIR/Pipfile"
python3 -m pipenv install

echo "Running "$1" ${@:2} ..."
python3 -m pipenv run "$1" ${@:2}
