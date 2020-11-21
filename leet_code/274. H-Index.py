import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        cnt = len(citations)
        
        for val in citations:
            if cnt <= val:
                return cnt
            cnt -= 1
        
        return 0


stime = time.time()
print(3 == Solution().hIndex(citations = [0,1,3,5,6]))
print('elapse time: {} sec'.format(time.time() - stime))

