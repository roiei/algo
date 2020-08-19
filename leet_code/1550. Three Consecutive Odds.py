
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def threeConsecutiveOdds(self, arr: [int]) -> bool:
        cnt = 0
        for num in arr:
            if num%2:
                cnt += 1
            else:
                cnt = 0

            if cnt >= 3:
                return True

        return False



stime = time.time()
print(False == Solution().threeConsecutiveOdds(arr = [2,6,4,1]))
print('elapse time: {} sec'.format(time.time() - stime))