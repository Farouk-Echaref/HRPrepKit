#!/usr/bin/bash

while read input;do
    echo "${input}" | cut -c 13-
done