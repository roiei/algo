import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return [0]
        
        def dfs(m):
            if m == 1:
                return ['0','1']
            
            x = dfs(m - 1)
            y = x[::-1]
            return ['0' + a for a in x] + ['1' + b for b in y]
        
        res = dfs(n)
        print(res)
        return [int(c, 2) for c in res]


  def grayCode(self, n):
        if n == 0:
            return [0]
        
        state = ['0', '1']
        
        for i in range(n - 1):
            next_state = []
            for i in range(len(state)):
                next_state += '0' + state[i],
            
            for i in range(len(state) - 1, -1, - 1):
                next_state += '1' + state[i],
            
            state = next_state
        
        return [int(val, 2) for val in state]


stime = time.time()
#print([0,1,3,2] == Solution().grayCode(2))
print(Solution().grayCode(3))
print('elapse time: {} sec'.format(time.time() - stime))


