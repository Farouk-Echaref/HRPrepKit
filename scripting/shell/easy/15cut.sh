#!/usr/bin/bash

while read input;do
    # print characters in the range 2 and 7 (included)
    echo $input | cut -b 2-7
done