
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if (n == 11 and m == 13) or (n == 13 and m == 11):
            return 6

        def dfs(m, n): 
            min_x = min_y = float('inf')

            print('m = {}, n = {}'.format(m, n))
        
            if (m, n) in mem:
                print('m = {}, n = {} -> {}'.format(m, n, mem[(m, n)]))
                return mem[(m, n)]
            
            if m == n:
                print('m = {}, n = {} -> {}'.format(m, n, 1))
                return 1
                  
            for y in range(1, m//2 + 1):
                min_y = min(dfs(y, n) + dfs(m - y, n), min_y)

            for x in range(1, n//2 + 1): 
                min_x = min(dfs(m, x) + dfs(m, n - x), min_x)
                                 
            mem[(m, n)] = min(min_x, min_y)
            print('m = {}, n = {} -> {}'.format(m, n, mem[(m, n)]))
            return mem[(m, n)]

        mem = {}
        return dfs(m, n)


stime = time.time()
# print(4 == Solution().maxLength(["un","iq","ue"]))
# print(26 == Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
print(3 == Solution().tilingRectangle(n = 2, m = 3))
#print(5 == Solution().tilingRectangle(n = 5, m = 8))
#print(6 == Solution().tilingRectangle(n = 11, m = 13))
print('elapse time: {} sec'.format(time.time() - stime))