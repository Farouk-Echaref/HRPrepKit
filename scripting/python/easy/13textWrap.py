#!/usr/bin/python3

import textwrap

def wrap(string: str, max_width: int):
    return (textwrap.fill(string, width))

if __name__ == "__main__":
    string, width = input(), int(input())
    result = wrap(string, width)
    print(result)