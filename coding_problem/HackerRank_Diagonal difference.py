import math
import os
import random
import re
import sys
 
def diagonalDifference(arr, n):
   lrds = 0
   rlds = 0
   for i in range(0, n):
       lrds += arr[i][i]
       rlds += arr[i][n-(1+i)]
   return abs(lrds - rlds)
 
if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')
   n = int(input())
   arr = []
   for _ in range(n):
       arr.append(list(map(int, input().rstrip().split()))
 
   result = diagonalDifference(arr, n)
   fptr.write(str(result) + '\n')
   fptr.close()