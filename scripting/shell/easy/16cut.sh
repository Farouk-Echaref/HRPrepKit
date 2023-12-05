#!/usr/bin/bash

while read input;do
    # Display the first four characters 
    echo $input | cut -b -4
done