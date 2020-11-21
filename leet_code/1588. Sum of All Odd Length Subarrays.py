
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""
    1  4  2  5  3
    -  -  -  -  -

    1  4  2  5  3
    -  -  -  -  -
    -------
       -------
          -------

    1  4  2  5  3
    -  -  -  -  -
    -------
       -------
          -------    
    -------------

    3  4  5  4  3


    1  4   2   5   3
  x 3  4   5   4   3
    3  16  10  20  9 = 58
"""

class Solution:
    def sumOddLengthSubarrays(self, arr: [int]) -> int:
        tot = 0
        n = len(arr)

        for i in range(1, n + 1, 2):
            for j in range(n - i + 1):
                tot += sum(arr[j:j + i])

        return tot

    def sumOddLengthSubarrays(self, arr: [int]) -> int:
        0  0  0
        -  -  -
        -------
        2  2  2

        0  0  0  0 
        -  -  -  -
        -------
           -------

        2  3  3  2


stime = time.time()
print(58 == Solution().sumOddLengthSubarrays([1,4,2,5,3]))
print('elapse time: {} sec'.format(time.time() - stime))


