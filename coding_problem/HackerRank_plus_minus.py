import math
import os
import random
import re
import sys
 
# Complete the plusMinus function below.
def plusMinus(arr):
   n = len(arr)
   num_pos = num_neg = num_zero = 0
   for i in range(n):
       if arr[i] > 0:
           num_pos += 1
       elif arr[i] < 0:
           num_neg += 1
       else:
           num_zero += 1
   print(num_pos/n)
   print(num_neg/n)
   print(num_zero/n)
 
if __name__ == '__main__':
   n = int(input())
   arr = list(map(int, input().rstrip().split()))
   plusMinus(arr)