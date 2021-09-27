
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


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

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])
        g = collections.defaultdict(list)
        
        for i in range(rows):
            for j in range(cols):
                if i == j:
                    continue

                if isConnected[i][j] == 0:
                    continue
                
                g[i] += j,
                g[j] += i,
        
        visited = set()
        cnt = 0

        for node in range(rows):
            if node in visited:
                continue

            q = [node]
            visited.add(node)
            
            while q:
                u = q.pop(0)
                
                for v in g[u]:
                    if v in visited:
                        continue
                    
                    visited.add(v)
                    q += v,
            
            cnt += 1
        
        return cnt


stime = time.time()
print(2 == Solution().findCircleNum([[1,1,0],
 [1,1,0],
 [0,0,1]]))
print('elapse time: {} sec'.format(time.time() - stime))