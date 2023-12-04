#!/usr/bin/bash

# concatenation of arrays in bash

# declaring empty arrays in bash
countries=()
newArr=()

# reading elements into the array
readarray -t countries
n=3

# concatenate the array into a new array n times
while [ $n -gt 0 ];do
    newArr+=( "${countries[@]}" )
    n=$(( n - 1 ))
done

# printing the new array
echo "${newArr[@]}"
