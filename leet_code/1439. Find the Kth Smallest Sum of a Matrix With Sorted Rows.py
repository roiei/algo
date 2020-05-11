
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def kthSmallest(self, mat: [[int]], k: int) -> int:
        q = [0]
        
        for line in mat:
            nq = []

            for elem in line:
                for val in q:
                    heapq.heappush(nq, val + elem)
            
            q = []
            i = 0
            while i < k and nq:
                q += heapq.heappop(nq),
                i += 1
        
        heapq.heapify(q)
        
        while k:
            val = heapq.heappop(q)
            k -= 1
        
        return val


    def kthSmallest2(self, mat: [[int]], k: int) -> int:
        q = [0]

        for line in mat:
            nq = []

            for elem in line:
                for val in q:
                    nq += val + elem,

            nq.sort()
            q = nq[:k]

        return q[-1]
        

stime = time.time()
print(9 == Solution().kthSmallest(mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7))
print('elapse time: {} sec'.format(time.time() - stime))