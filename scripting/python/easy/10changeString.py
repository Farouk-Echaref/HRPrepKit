#!/usr/bin/python3

# change immutable string
# function to return new string
def mutate_string(string, position, character) -> str:

    #convert string to a temporary string so we can change it's values
    tmp: list = list(string)

    # change character at pos - 1
    tmp[position] = character

    #join the string back
    string = "".join(tmp)

    # return the new changed string
    return (string)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)