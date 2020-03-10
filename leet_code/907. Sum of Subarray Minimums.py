
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stk = []
        tot = inc = 0
        
        for val in A:
            cnt = 1
            
            while stk and stk[-1][0] >= val:
                v, c = stk.pop()
                cnt += c
                inc -= v*c
            
            stk += (val, cnt),
            inc += val*cnt
            tot += inc
            
        return tot % (10**9 + 7)
    
    
    def sumSubarrayMins(self, A: List[int]) -> int:
        res = []
        res += list(A),

        for i in range(1, len(A)):
            cur = []
            for j in range(len(A) - i):
                cur += min(res[-1][j], res[-1][j + 1]),
            res += cur,

        tot = 0
        for r in res:
            tot += sum(r)

        if tot > 10**9 + 7:
            tot = tot % (10**9 + 7)
        return tot


stime = time.time()
print(17 == Solution().minAddToMakeValid([3,1,2,4]))
print('elapse time: {} sec'.format(time.time() - stime))