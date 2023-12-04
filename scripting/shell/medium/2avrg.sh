#!/usr/bin/bash

read IN
SUM=0
hold=$IN
while [ $IN -gt 0 ]
do
    read NUM
    SUM=$(( SUM + NUM ))
    IN=$(( IN - 1 ))
done

avg=$(echo "$SUM / $hold" | bc -l)
rounded_number=$(printf "%.3f" "$avg")

echo "$rounded_number"