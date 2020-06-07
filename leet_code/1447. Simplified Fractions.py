
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        done = []
        res = []
        
        for i in range(2, n + 1):
            for j in range(1, i):
                fraction = j/i
                if fraction in done:
                    continue
                
                done += fraction,
                res += '{}/{}'.format(j, i),
        
        return res


stime = time.time()
print(["1/2","1/3","1/4","2/3","3/4"] == Solution().simplifiedFractions(n = 4))
print('elapse time: {} sec'.format(time.time() - stime))