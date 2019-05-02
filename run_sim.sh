#!/bin/bash

chmod u+x run_sim.sh

if [ "$#" -ne 1 ]; then
    echo "invalid number of argument"
fi

run.py -s 16KB -a 32 -f $1

run.py -s 32KB -a 32 -f $1

run.py -s 32KB -a 16 -f $1

run.py -s 32KB -a 8 -f $1

run.py -s 4MB -a 16 -f $1

run.py -s 4MB -a 8 -f $1

