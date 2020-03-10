
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        freq = collections.Counter(arr)
        freq = sorted(freq.items(), key=lambda p: p[1], reverse=True)
        
        n = (len(arr) + 1)//2
        cnt = 0
        
        while n > 0:
            n -= freq.pop(0)[1]
            cnt += 1
        
        return cnt
        

            
stime = time.time()
print(2 == Solution().kWeakestRows(arr = [3,3,3,3,5,5,5,2,2,7]))
print('elapse time: {} sec'.format(time.time() - stime))