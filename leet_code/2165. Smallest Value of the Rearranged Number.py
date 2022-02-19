
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List



class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = list(str(num))
        zero = 0
        res = []
        sign = 1

        if nums and nums[0] == '-':
            sign = -1
            nums.pop(0)
            nums.sort(reverse=True)
        else:
            nums.sort()

        if sign == 1:
            for num in nums:
                if num == '0':
                    zero += 1
                    continue

                res += num,

            res[1:1] = ['0']*zero
        else:
            for num in nums:
                res += num,

        print(res)
        return sign*int(''.join(res))






stime = time.time()
print(-7650 == Solution().smallestNumber(num=-7605))
print(103 == Solution().smallestNumber(num=310))
print('elapse time: {} sec'.format(time.time() - stime))