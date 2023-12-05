#!/usr/bin/bash

while read input;do
    # print the second and the third characters
    echo $input | cut -b 2,7
done