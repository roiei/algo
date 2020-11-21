import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def getPermutation(self, n: int, k: int) -> str:
        #      1*1  1*2  2*3  6*4
        # 1    1    2    6    24
        
        nums = [i for i in range(1, n + 1)]
        factorial = [1]
        
        for i in range(1, n + 1):
            factorial += factorial[-1]*i,
        
        res = []
        for i in range(n - 1, -1, -1):
            idx = (k - 1)//factorial[i]
            res += nums.pop(idx),
            k -= idx*factorial[i]
        
        return ''.join([str(i) for i in res])


stime = time.time()
print(Solution().getPermutation(4, 13))
print('elapse time: {} sec'.format(time.time() - stime))