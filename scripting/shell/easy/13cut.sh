#!/usr/bin/bash

while read input;do
    # print the third character
    echo $input | cut -b 3
done