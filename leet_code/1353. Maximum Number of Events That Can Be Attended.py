
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        cnt = 0
        used = set()
        
        for s, e in events:
            s -= 1
            while s < e:
                if s in used:
                    s += 1
                    continue
                
                used.add(s)
                cnt += 1
                break
        
        return cnt
        
            
stime = time.time()
print(3 == Solution().maxEvents([[1,2],[1,2],[1,6],[1,2],[1,2]]))
print(4 == Solution().maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))
print(4 == Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]]))
print('elapse time: {} sec'.format(time.time() - stime))