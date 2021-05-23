import time
import re
import collections
from typing import List
import itertools


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        for ftype, fday, cap in queries:
            rs = sum(candiesCount[:ftype])

            print(ftype, fday, cap)
            print(rs, fday)
            print()

            if fday - rs > 0:
                if candiesCount[ftype] - (fday - rs) > 0:
                    res += True,
                else:
                    res += False,
            else:
                if rs > fday*cap:
                    res += False,
                else:
                    res += True,
            
        print(res)
        return res

    def canEat(self, candiesCount, queries):
        A = [0] + list(itertools.accumulate(candiesCount))

        res = []
        for t, d, c in queries:
            res += A[t] // c <= d < A[t + 1],

        return res


stime = time.time()
# print([True,False,True] == Solution().canEat(candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]))
print([False,True,True,False,False] == Solution().canEat([5,2,6,4,1], 
[[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]))
print('elapse time: {} sec'.format(time.time() - stime))