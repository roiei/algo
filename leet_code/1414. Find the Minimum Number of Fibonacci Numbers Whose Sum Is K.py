
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        seq = [1, 1]
        while seq[-1] < k:
            seq += seq[-2] + seq[-1],
        
        cnt = 0
        
        while k:
            while k < seq[-1]:
                seq.pop()
            
            val = seq.pop()
            k -= val
            cnt += 1
            
        return cnt
        

stime = time.time()
print(5 == Solution().findMinFibonacciNumbers([-3,2,-3,4,2]))
print('elapse time: {} sec'.format(time.time() - stime))