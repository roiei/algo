
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def circularPermutation(self, n: int, start: int) -> [int]:
        
        shift = 0
        seq = [0]
        
        for shift in range(n):
            news = []
            for val in seq:
                news.insert(0, val | (1<<shift))
            seq += news
        
        idx = seq.index(start)
        return seq[idx:] + seq[:idx]
   

stime = time.time()
#print([2,6,7,5,4,0,1,3] == Solution().circularPermutation(3, 2))
print([1,3,2,6,7,5,4,12,13,15,14,10,11,9,8,0] == Solution().circularPermutation(4, 1))
print('elapse time: {} sec'.format(time.time() - stime))