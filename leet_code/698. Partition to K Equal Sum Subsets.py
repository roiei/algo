import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def canPartitionKSubsets_ref(self, nums, k):
        if not nums or not k or 0 != sum(nums)%k:
            return False

        def dfs(start, inc, k, used): 
            if k == 1:
                return True
            if inc > part:
                return False
            if inc == part:
                return dfs(0, 0, k-1, used)

            for i in range(start, n):
                if used[i] == True:
                    continue
                used[i] = True
                if dfs(i+1, inc + nums[i], k, used):
                    return True
                used[i] = False
            return False

        part = sum(nums)//k
        n = len(nums)
        used = [False]*n
        return dfs(0, 0, k, used)


    def canPartitionKSubsets(self, nums, k):
        if not nums or not k or 0 != sum(nums)%k:
            return False

        def dfs(nums, n, k, start, used, part, inc):
            if k == 1:
                return True
            if inc > part:
                return False
            if inc == part:
                inc = 0
                k -= 1
                start = 0

            for i in range(start, n):
                if used[i] == True:
                    continue
                used[i] = True
                if dfs(nums, n, k, i+1, used, part, inc + nums[i]):
                    return True
                used[i] = False
            return False

        used = [False]*len(nums)
        return dfs(nums, len(nums), k, 0, used, sum(nums)//k, 0)


    def canPartitionKSubsets(self, nums, k):
        if not nums or not k or 0 != sum(nums)%k:
            return False

        n = len(nums)
        part = sum(nums)//k
        
        def dfs(nums, start, n, left, k, skip):
            if left < 0:
                return False
        
            if left == 0:
                left = part
                k -= 1
                start = 0

            if k == 0:
                return True
            
            for i in range(start, n):
                if i in skip:
                    continue
                skip += i,
                if True == dfs(nums, i+1, n, left - nums[i], k, skip):
                    return True
                skip.pop()

            return False
            
        return dfs(nums, 0, n, part, k, [])


stime = time.time()
# print(Solution().canPartitionKSubsets_ref([4, 3, 2, 3, 5, 2, 1], 4))
# print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
print(Solution().canPartitionKSubsets_ref([5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,3], 15))
print(Solution().canPartitionKSubsets([5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,3], 15))
print('elapse time: {} sec'.format(time.time() - stime))


