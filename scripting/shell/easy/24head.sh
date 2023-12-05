#!/usr/bin/bash

while read input;do
    echo "${input}" >> in
done


# print the lines from line number 12 to 22, both inclusive (tail -(22 - 11 + 1))
head -n 22 in | tail -11