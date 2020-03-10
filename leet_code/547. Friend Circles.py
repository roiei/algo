
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = set()
        cnt = 0
        
        for i in range(n):
            if i in visited:
                continue
            
            q = [i]
            while q:
                u = q.pop(0)
                for v in range(len(M[u])):
                    if M[u][v] == 1 and v not in visited:
                        visited.add(v)
                        q += v,
            cnt += 1
        
        return cnt


stime = time.time()
print(2 == Solution().findCircleNum([[1,1,0],
 [1,1,0],
 [0,0,1]]))
print('elapse time: {} sec'.format(time.time() - stime))