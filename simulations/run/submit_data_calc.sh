#!/bin/bash
module load gcc/10.5.0
module load cuda/12.2.1
python continue.py -n 16000 -l 50.0  -t 100000 -p 0.48  > out.out 2>&1
