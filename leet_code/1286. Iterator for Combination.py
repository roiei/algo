
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        cobms = []
        n = len(characters)
        
        def do(start, seq, res):
            if len(seq) == combinationLength:
                res += ''.join(seq),
                return
            
            for i in range(start, n):
                do(i + 1, seq + [characters[i]], res)
        
        self.res = []
        do(0, [], self.res)
        
        self.n = len(self.res)
        self.pos = 0

    def next(self) -> str:
        ret = None

        if self.pos < self.n:
            ret = self.res[self.pos]
            self.pos += 1
        return ret

    def hasNext(self) -> bool:
        return self.pos < self.n
            
            
stime = time.time()
itor = CombinationIterator("abc", 2)
#print(2 == Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]))
print('elapse time: {} sec'.format(time.time() - stime))