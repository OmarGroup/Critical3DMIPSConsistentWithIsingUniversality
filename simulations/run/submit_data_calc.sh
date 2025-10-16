#!/bin/bash
#SBATCH --account=fc_omargroup
#SBATCH --partition=savio3_gpu
#SBATCH --qos=gtx2080_gpu3_normal
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:GTX2080TI:1
#SBATCH --time=11:00:00
#SBATCH --output=hoomd3.out

module load gcc/10.5.0
module load cuda/12.2.1
python continue.py -n 16000 -l 50.0  -t 100000 -p 0.48  > out.out 2>&1
