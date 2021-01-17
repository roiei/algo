
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            val = arr.pop(i)
            
            if val + val in arr:
                return True
            
            arr.insert(i, val)
        
        return False

    def checkIfExist(self, arr: List[int]) -> bool:
        freq = collections.Counter(arr)

        for num in arr:
            dnum = num + num
            if dnum in freq:
                if (freq[dnum] == 2 and dnum == num) or \
                (freq[dnum] == 1 and dnum != num):
                    return True

        return False

            
stime = time.time()
print(True == Solution().checkIfExist([10,2,5,3]))
print(True == Solution().checkIfExist([0, 0]))
print('elapse time: {} sec'.format(time.time() - stime))