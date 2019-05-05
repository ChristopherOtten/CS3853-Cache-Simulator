#!/bin/bash

chmod u+x run_sim.sh

if [ "$#" -ne 1 ]; then
    echo "invalid number of argument"
fi

run.py -s 1MB -a 16 -f $1

