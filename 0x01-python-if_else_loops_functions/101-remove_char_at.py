#!/usr/bin/python3
def remove_char_at(str, n):
    temp_str = str
    if (str):
        str = str[:n] + str[n + 1:]
    if (n < 0):
        str = temp_str
    return (str)
