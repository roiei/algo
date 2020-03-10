import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq



class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        def sort_merge(nums, l, r):
            if l >= r:
                return
            m = (l+r)//2
            sort_merge(nums, l, m)
            sort_merge(nums, m+1, r)

            llen = m-l+1
            rlen = r-m
            left = nums[l:l+llen]
            right = nums[m+1:m+1+rlen]

            li = ri = 0
            for i in range(l, r+1):
                if li >= llen:
                    nums[i] = right[ri]
                    ri += 1
                    continue
                elif ri >= rlen:
                    nums[i] = left[li]
                    li += 1
                    continue
                if left[li] < right[ri]:
                    nums[i] = left[li]
                    li += 1
                else:
                    nums[i] = right[ri]
                    ri += 1

        sort_merge(nums, 0, len(nums)-1)
        return nums


stime = time.time()
print([1,2,3,5] == Solution().sortArray([5,2,3,1]))
print('elapse time: {} sec'.format(time.time() - stime))


