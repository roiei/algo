import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if '' == num:
            return '0'        
        n = len(num)
        res = [num[0]]
        for i in range(1, n):
            while k > 0 and res and res[-1] > num[i]:
                res.pop()
                k -= 1
            res += num[i],
        while k > 0:
            res.pop()
            k -= 1
        while res and '0' == res[0]:
            res.pop(0)
        return '0' if not res else ''.join(res)



stime = time.time()
print('200' == Solution().removeKdigits("10200", k=1))
# print('11' == Solution().removeKdigits("112", k=1))
# print('0' == Solution().removeKdigits("10", k=1))
# print('1219' == Solution().removeKdigits("1432219", k=3))
print('elapse time: {} sec'.format(time.time() - stime))