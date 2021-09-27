import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq



class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        def dfs(n):
            if n in mem:
                return mem[n]

            if n >= 2:
                if n%2 == 0:
                    res = dfs(n//2)*dfs(n//2)
                    mem[n] = res
                    return res

                left = n - (n//2)*2
                res = dfs(n//2)*dfs(n//2 + left)
                mem[n] = res
                return res

            if n == 1:
                return x

        mem = {}
        val = dfs(abs(n))
        if n < 0:
            return 1/val
        return val


stime = time.time()
print(1024.00000 == Solution().myPow(2.00000, 10))
print(9.26100 == Solution().myPow(2.10000, 3))
print(0.25000 == Solution().myPow(2.00000, -2))
print('elapse time: {} sec'.format(time.time() - stime))


