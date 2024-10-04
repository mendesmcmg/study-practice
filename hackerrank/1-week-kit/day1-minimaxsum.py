#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total_sum = sum(arr)
    mini = min(arr)
    maxi = max(arr)
    
    minisum = total_sum - maxi
    maxisum = total_sum - mini
    
    print(f"{minisum} {maxisum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
