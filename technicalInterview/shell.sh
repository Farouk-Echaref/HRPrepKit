#!/usr/bin/sh

array=()

# read elements into an array
readarray -t array

#join elements of the array
newElemString="${array[*]}"

# change case of the string using awk scripting tool
convertedString=$(echo "$newElemString" | awk '{print tolower($0)}')
