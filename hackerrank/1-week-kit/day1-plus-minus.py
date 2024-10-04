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
  length = len(arr)  
  pos_count = sum(1 for x in arr if x > 0)
  neg_count = sum(1 for x in arr if x < 0)
  zero_count = sum(1 for x in arr if x == 0)

  pos_ratio = pos_count / length
  neg_ratio = neg_count / length
  zero_ratio = zero_count / length

  print(f"{pos_ratio:.6f}")
  print(f"{neg_ratio:.6f}")
  print(f"{zero_ratio:.6f}")
        

if __name__ == '__main__':
  n = int(input().strip())

  arr = list(map(int, input().rstrip().split()))

  plusMinus(arr)
