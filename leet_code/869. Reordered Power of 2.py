
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def reorderedPowerOf2(self, N):
        val = sorted([int(ch) for ch in str(N)], reverse=True)
        mx = int(''.join([str(digit) for digit in val]))
        n_freq = collections.Counter(str(N))

        shift = 0
        while 1<<shift <= mx:
            digits = collections.Counter(str(1<<shift))
            if n_freq == digits:
                return True
            shift += 1
        
        return False


stime = time.time()
# print(True == Solution().reorderedPowerOf2(1))
# print(False == Solution().reorderedPowerOf2(10))
# print(True == Solution().reorderedPowerOf2(16))
print(True == Solution().reorderedPowerOf2(46))
# print(False == Solution().reorderedPowerOf2(24))
print('elapse time: {} sec'.format(time.time() - stime))