
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        outdegree = collections.defaultdict(int)
        g = collections.defaultdict(list)
        for u, v in trust:
            outdegree[u] += 1
            g[v] += u,
        
        res = -1
        for i in range(1, N + 1):
            if outdegree[i] == 0:
                res = i
        
        if res != -1:
            cnt = 0
            for i in range(1, N + 1):
                if i == res:
                    continue
                
                if i in g[res]:
                    cnt += 1
            
            if cnt == N - 1:
                return res
        
        return -1
        

stime = time.time()
print('c' == Solution().getHappyString(n = 1, k = 3))
print('' == Solution().getHappyString(n = 1, k = 4))
print('cab' == Solution().getHappyString(n = 3, k = 9))
print('' == Solution().getHappyString(n = 2, k = 7))
print('abacbabacb' == Solution().getHappyString(n = 10, k = 100))
print('elapse time: {} sec'.format(time.time() - stime))