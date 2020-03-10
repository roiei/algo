import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def zegZagIterator(self, vectors):
        if not vectors:
            return []
        out = []
        n = len(vectors)
        while n:
            for v in vectors:
                if not v:
                    n -= 1
                    continue
                out += v.pop(0),
        return out

    def zegZagIterator(self, vectors):
        if not vectors:
            return []
        res = []
        n = len(vectors)

        while vectors:
            for v in vectors:
                if not v:
                    continue
                res += v.pop(0),
            vectors = [v for v in vectors if v]
        
        return res


stime = time.time()
print(Solution().zegZagIterator([[1, 2], [3, 4, 5, 6]]))
print(Solution().zegZagIterator([[1,2,3],[4,5,6,7],[8,9]]))
print('elapse time: {} sec'.format(time.time() - stime))