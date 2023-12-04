#!/usr/bin/bash

read -r IN

res=`echo "$IN" | bc -l`
rounded_number=$(printf "%.3f" "$res")
# echo $(expr $IN)

echo $rounded_number