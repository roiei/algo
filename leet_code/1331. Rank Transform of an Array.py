
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        
        arr = sorted([(i, val) for i, val in enumerate(arr)], key=lambda p: p[1], reverse=False)
        n = len(arr)
        res = [0]*n
        rank = 1
        
        res[arr[0][0]] = rank
        
        for i in range(1, n):
            if arr[i][1] > arr[i - 1][1]:
                rank += 1
            
            res[arr[i][0]] = rank
        
        return res

            
stime = time.time()
print([4,1,2,3] == Solution().arrayRankTransform(arr = [40,10,20,30]))
print('elapse time: {} sec'.format(time.time() - stime))