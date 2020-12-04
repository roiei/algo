
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def decrypt(self, code: [int], k: int) -> [int]:
        res = []
        n = len(code)
        reversed = False
        
        if k < 0:
            code = code[::-1]
            k *= -1
            reversed = True
        
        for i, num in enumerate(code):
            start = (i + 1)%n
            end = (start + k)%n

            if start > end:
                res += sum(code[start:] + code[:end]),
            else:
                res += sum(code[start:end]),
        
        return res if not reversed else res[::-1]


stime = time.time()
#print([12,10,16,13] == Solution().decrypt(code = [5,7,1,4], k = 3))
print([12,5,6,13] == Solution().decrypt(code = [2,4,9,3], k = -2))
print('elapse time: {} sec'.format(time.time() - stime))


# 2 4 9 3

# 3 9 4 2