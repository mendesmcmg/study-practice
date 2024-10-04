#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    negs, zero, pos = 0, 0, 0
    for number in arr:
        if number > 0:
            pos+=1
        elif number == 0:
            zero+=1
        else:
            negs+=1
    negratio = negs/len(arr)
    posratio = pos/len(arr)
    zeroratio = zero/len(arr)
    print("{:.6f}".format(posratio))
    print("{:.6f}".format(negratio))
    print("{:.6f}".format(zeroratio))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
