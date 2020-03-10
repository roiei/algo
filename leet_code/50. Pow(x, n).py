import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq



class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = n
        nums = []
        while 0 == num%2:
            num //= 2
            nums += 2,
        nums += num,

        print('nums = ', nums)

        for num in nums:
            val = 1
            for i in range(num):
                #print('val {} = val {} * x {}'.format(val*x, val, x))
                val *= x
            x = val
            #print('x = ', x)
        return val


stime = time.time()
print(Solution().myPow(2.00000, 10))
print(Solution().myPow(2.10000, 3))
print('elapse time: {} sec'.format(time.time() - stime))


