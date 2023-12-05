#!/usr/bin/bash

while read input;do
    echo "${input}" | cut -d $'\t' -f2-
done