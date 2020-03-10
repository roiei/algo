
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def maxAverage(self, nums, k):
        l = min(nums)
        r = max(nums)

        def hasAverageAbove(nums, k, mid):
            num_diffs = list(map(lambda x: x - mid, nums))
            pre_tot = 0
            n = len(num_diffs)
            tot = sum(num_diffs[:k])

            print(num_diffs)
            print(tot)

            if tot >= 0: 
                return True

            for i in range(k, n):
                tot += num_diffs[i]
                pre_tot += num_diffs[i - k]
                if pre_tot < 0:
                    tot -= pre_tot
                    pre_tot = 0
                if tot > 0:
                    return True
            return False

        while l + 10**-5 < r:
            mid = (l + r) / 2.0
            if hasAverageAbove(nums, k, mid):
                l = mid
            else:
                r = mid

        print(r)
        return r


    


stime = time.time()
print(15.666670799255371 == Solution().maxAverage([1,12,-5,-6,50,3], 3)) # "eceb"
print('elapse time: {} sec'.format(time.time() - stime))