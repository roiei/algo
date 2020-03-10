
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        nums = []
        for i, line in enumerate(mat):
            nums += (i, line.count(1)),
        
        nums.sort(key=lambda p: p[1], reverse=False)
        return [i for i, val in nums[:k]]

            
stime = time.time()
print([2,0,3] == Solution().kWeakestRows(mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], k = 3))
print('elapse time: {} sec'.format(time.time() - stime))