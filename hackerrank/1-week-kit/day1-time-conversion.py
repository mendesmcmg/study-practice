#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
  hours, mins, secs = s[:-2].split(":")
  ampm = s[-2:]

  if ampm == "PM" and hours != "12":
      hours = str(int(hours) + 12)
  elif ampm == "AM" and hours == "12":
      hours = "00"
    
    # Ensure hours are always two digits
  military_time = f"{hours.zfill(2)}:{mins}:{secs}"
  return military_time

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  s = input()

  result = timeConversion(s)

  fptr.write(result + '\n')

  fptr.close()
