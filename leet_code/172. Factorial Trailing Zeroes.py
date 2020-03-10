import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def trailingZeroes_to(self, n: int) -> int:
        nums = [i for i in range(n, 0, -1)]
        tot = 1
        for i in range(len(nums)):
            tot *= nums[i]
        
        tot = list(str(tot))
        cnt = 0
        for i in range(len(tot)-1, -1, -1):
            if tot[i] == '0':
                cnt += 1
            else:
                break
        return cnt

    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n > 0:
            n //= 5
            cnt += n
        return cnt


stime = time.time()
print(Solution().trailingZeroes(3865))
print('elapse time: {} sec'.format(time.time() - stime))