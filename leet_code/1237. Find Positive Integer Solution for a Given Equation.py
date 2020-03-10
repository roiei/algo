
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> [[int]]:

        def dfs(x, y, res):
            if (x, y) in mem:
                return

            ret = customfunction.f(x, y)
            if ret > z:
                return
            
            if ret == z and (x, y) not in res:
                res += (x, y),
            
            dfs(x + 1, y, res)
            dfs(x, y + 1, res)
            mem[(x, y)] = True
        
        mem = {}
        res = []
        dfs(1, 1, res)
        return res
   

stime = time.time()
#print("012" == Solution().originalDigits("owoztneoer"))
#print("9" == Solution().originalDigits("nnei"))
print("00" == Solution().findSolution(1, 25))
print('elapse time: {} sec'.format(time.time() - stime))