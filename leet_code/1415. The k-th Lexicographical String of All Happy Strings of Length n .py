
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def dfs(seq, pos, res, n):
            nonlocal k

            if n == 0:
                k -= 1
                if k == 0:
                    res[0] = seq
                return
            
            for ch in 'abc':
                if pos - 1 >= 0 and seq[pos - 1] == ch:
                    continue
                
                dfs(seq + [ch], pos + 1, res, n - 1)
        
        res = ['']
        dfs([], 0, res, n)
        return ''.join(res[0])
        

stime = time.time()
print('c' == Solution().getHappyString(n = 1, k = 3))
print('' == Solution().getHappyString(n = 1, k = 4))
print('cab' == Solution().getHappyString(n = 3, k = 9))
print('' == Solution().getHappyString(n = 2, k = 7))
print('abacbabacb' == Solution().getHappyString(n = 10, k = 100))
print('elapse time: {} sec'.format(time.time() - stime))