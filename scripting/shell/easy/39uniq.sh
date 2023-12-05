#!/usr/bin/bash

# -i: case insensitive
uniq -c -i | awk '{$1=$1;print}'