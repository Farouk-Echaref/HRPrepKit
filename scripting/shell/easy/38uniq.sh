#!/usr/bin/bash

# count occurrence of lines in file
# When this expression is executed, awk interprets it as updating the value of the first field to itself, which triggers the rebuilding of the entire record.
# The effect of this is to remove leading and trailing whitespaces from the record and to reformat the output using the default field separator (whitespace).


uniq -c | awk '{$1=$1;print}'