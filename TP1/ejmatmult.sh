#!/bin/bash
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH -o ./outputs/outputmult.txt
#SBATCH -e ./outputs/errorsmult.txt
./mat_mult $1 $2
