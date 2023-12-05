#!/usr/bin/bash

while read -r input;do
    echo "${input}" | tr '()' '[]'
done
echo "${input}" | tr '()' '[]'

# or could simply use in hackerrank :
# tr '()' '[]'