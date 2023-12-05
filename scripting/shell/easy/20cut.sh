#!/usr/bin/bash

while read input;do
    echo "${input}" | cut -d ' ' -f1-3
done