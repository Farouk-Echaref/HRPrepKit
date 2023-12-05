#!/usr/bin/bash

while read input;do
    # print from the first field to the third field on each line using tab as delimiter
    # use double quotes to prevent unintended word splitting and globbing (line may contain multiple spaces)
    echo "${input}" | cut -d $'\t' -f -3
done