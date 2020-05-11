
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> [int]:
        mn = float('inf')
        mx = float('-inf')
        
        def dfs(a, b, c, depth):
            nonlocal mx
            nonlocal mn
            
            if a + 1 == b and b + 1 == c:
                print(a, b, c, depth)
                mx = max(mx, depth)
                mn = min(mn, depth)
                return
        
            if a + 1 < b:
                dfs(a + 1, b, c, depth + 1)
                dfs(b - 1, b, c, depth + 1)
            
            if b + 1 < c:
                dfs(a, b, c - 1, depth + 1)
                dfs(a, b, b + 1, depth + 1)
        
        dfs(a, b, c, 0)
        return [mn, mx]

    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        (a, b, c) = tuple(sorted([a, b, c]))
        if c - a == 2:
            return (0, 0)
        if c - b == 1:
            return (1, b - a - 1)
        if b - a == 1:
            return (1, c - b - 1)
        if b - a == 2:
            return (1, c - a - 2)
        if c - b == 2:
            return (1, c - a - 2)
        return (2, c - a - 2)
        

stime = time.time()
#print([1,2] == Solution().numMovesStones(a = 1, b = 2, c = 5))
print([1,2] == Solution().numMovesStones(3, 5, 1))
print('elapse time: {} sec'.format(time.time() - stime))

