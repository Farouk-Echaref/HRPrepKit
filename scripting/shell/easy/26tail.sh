#!/usr/bin/bash

while read input;do
    echo "${input}" >> in
done

# display the last 20 characters
tail -c 20 in