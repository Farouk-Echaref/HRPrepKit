#!/usr/bin/bash

# show only the lines that contains these exact patterns not substrings, case insensitive
grep -i -w -e "pat1" -e "pat2" -e "pat3"