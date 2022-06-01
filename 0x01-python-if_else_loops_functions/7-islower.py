#!/usr/bin/python3
def islower(c):
    asciiValue = ord(c)
    if asciiValue >= 97 and asciiValue <= 122:
        return True
    return False
