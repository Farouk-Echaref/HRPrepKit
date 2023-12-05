#!/usr/bin/bash

while read line;do
    echo "${line}" >> in.txt
done

#  order the lines in lexicographical order.
cat in.txt | sort -n -r