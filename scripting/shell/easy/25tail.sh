#!/usr/bin/bash

while read input;do
    echo "${input}" >> in
done

# display the last 20 lines²
tail -20 in