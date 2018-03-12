#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "Options:"
    echo "lint:"
    echo "  Run pylint to check conformance to coding standards"
fi

if [[ $1 = "lint" ]]; then
    CMD="pylint ./app ./reallocate/ config.py manage.py"
    eval $CMD
fi