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
  ihours = int(hours)

  if ampm == "PM":
    if ihours != 12:
      ihours += 12
  else:
    if ihours == 12:
      ihours = 0
  hours = str(ihours)
  if ihours < 10:
      hours = "0" + hours
  military_time = ":".join([hours, mins, secs])
  return military_time

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  s = input()

  result = timeConversion(s)

  fptr.write(result + '\n')

  fptr.close()
