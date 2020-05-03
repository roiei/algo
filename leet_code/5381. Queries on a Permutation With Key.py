
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def processQueries(self, queries: [int], m: int) -> [int]:
        p = list(range(1, m + 1))
        res = []
        for q in queries:
            idx = p.index(q)
            res += idx,
            val = p.pop(idx)
            p.insert(0, val)
        
        return res


stime = time.time()
print([3,1,2,0] == Solution().processQueries(queries = [4,1,2,2], m = 4))
print('elapse time: {} sec'.format(time.time() - stime))