
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(map(int, list(str(n))))
        product = 1
        tot = 0

        for i in range(len(nums)):
            product *= nums[i]
            tot += nums[i]

        return product - tot

        

stime = time.time()
print(15 == Solution().subtractProductAndSum(n = 234))
print(21 == Solution().subtractProductAndSum(n = 4421))
print('elapse time: {} sec'.format(time.time() - stime))