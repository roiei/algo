import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def getStrongest(self, arr: [int], k: int) -> [int]:
        arr.sort()
        n = len(arr)
        m = arr[(n - 1)//2]
        
        vals = collections.defaultdict(list)
        for num in arr:
            vals[abs(num - m)] += num,
        
        vals = sorted(vals.items(), key=lambda p: p[0], reverse=True)
        res = []
        
        for key, v in vals:
            v = sorted(v, reverse=True)
            for num in v:
                if not k:
                    return res
                res += num,
                k -= 1
        
        return res
        

stime = time.time()
print([5,1] == Solution().getStrongest(arr = [1,2,3,4,5], k = 2))
print('elapse time: {} sec'.format(time.time() - stime))

     