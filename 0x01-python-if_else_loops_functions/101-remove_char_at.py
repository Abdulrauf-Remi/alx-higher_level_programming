#!/usr/bin/python3
def remove-char_at(str, n):
    return (str[0:n] + str[n+1:] if n >= 0 else str)
