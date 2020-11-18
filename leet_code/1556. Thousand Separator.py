
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = list(str(n))
        n = len(num)
        res = []
        
        num_separators = n//3
        
        for i in range(num_separators):
            for j in range(3):
                res.insert(0, num.pop())
            
            if num:
                res.insert(0, '.')
        
        while num:
            res.insert(0, num.pop())
        
        return ''.join(res)


stime = time.time()
print("987" == Solution().thousandSeparator(987))
print('elapse time: {} sec'.format(time.time() - stime))
