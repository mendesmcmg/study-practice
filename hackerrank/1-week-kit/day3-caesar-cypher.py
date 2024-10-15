#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def char_index(char, k):
    move = ord(char) + (k % 26)
    subtractlow = -26 if char.islower() and move > ord('z') else 0
    subtractup = -26 if char.isupper() and move > ord('Z') else 0
    return move + subtractlow + subtractup

def caesarCipher(s, k):
    cypher = ""
    for char in s:
        if char.isalpha():
            cypher += chr(char_index(char, k))
        else:
            cypher += char
    return cypher

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
