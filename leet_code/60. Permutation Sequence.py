import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def getPermutation(self, n: int, k: int) -> str:
        nums = [num for num in range(1, n+1)]
        factorial = [1]
        # 1*1  1*1  1*2  2*3  6*4
        # 1    1    2    6    24
        for i in nums:
            factorial += factorial[-1]*i,

        print('nums = ', nums)
        print('factorial = ', factorial)

        r = ''
        for i in range(n):
            idx = (k-1)//factorial[n-1-i]
            print('idx = {}, k = {}, i = {}, factorial val = {}'.format(idx, k, i, factorial[n-1-i]))
            r += str(nums[idx])
            print('r = ', r)
            nums.pop(idx)
            k = k - factorial[n-1-i]*idx
        return r


stime = time.time()
print(Solution().getPermutation(4, 13))
print('elapse time: {} sec'.format(time.time() - stime))