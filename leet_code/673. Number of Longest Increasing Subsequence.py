import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findNumberOfLIS(self, nums: [int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == nums.count(nums[0]):
            return n
        dp = [1]*n
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[i]+1, dp[j])
                    print(dp[j])
        # dp
        # 1 2 3 3 4

        print(dp)

        ndp = [1]*n
        mlen = 0
        freq = {}


        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    ndp[j] = max(ndp[i]+1, ndp[j])
                    print('[{}] = {}'.format(j, ndp[j]))
                    #print(ndp[j])


                if mlen <= ndp[j]:
                    mlen = ndp[j]
                    if mlen not in freq:
                        freq[mlen] = 0
                    freq[mlen] += 1

        print(freq)
        #freq.sort(key=lambda p:p[0], reverse=True)
        #print(freq, freq[0][1])
        #return freq[0][1]

    def findNumberOfLIS(self, nums: [int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        lengths = [0]*n       # lengths[i] = longest ending in nums[i]
        counts = [1]*n        # count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] >= nums[j]:
                    continue
                    
                if lengths[i] >= lengths[j]:
                    lengths[j] = 1 + lengths[i]
                    counts[j] = counts[i]
                elif lengths[i] + 1 == lengths[j]:
                    counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)



stime = time.time()
#print(5 == Solution().findNumberOfLIS([2, 2, 2, 2, 2]))
print(3 == Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]))
#print(2 == Solution().findNumberOfLIS([1,3,5,4,7]))
print('elapse time: {} sec'.format(time.time() - stime))