#!/bin/bash

headers="Block Size, 512, 1024, 2048, 4096"
echo $headers > ./outputs/time_bs.csv
echo
for i in {3..9}; do
    bs=$((2 ** i))
    dim=256
    row="$bs"
    for j in {1..4}; do
        dim=$((dim * 2))
        sbatch --wait ./ejmatmult.sh $dim $bs
        exTime=$(cat ./outputs/outputmult.txt)
        row="$row,$exTime"
    done
    echo $row >> ./outputs/time_bs.csv
    echo
done
