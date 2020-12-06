import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        
        while True:
            pre_len = len(nums)
            l = 0
            r = len(nums) - 1
            
            while l < r:
                s = nums[l] + nums[r]
                if s == k:
                    nums.pop(r)
                    nums.pop(l)
                    break
                if s > k:
                    r -= 1
                else:
                    l += 1
                
            if pre_len == len(nums):
                break

            cnt += 1
        
        return cnt

    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        
        while nums:
            num = nums.pop(0)
            if k - num in nums:
                idx = nums.index(k - num)
                nums.pop(idx)
                cnt += 1
            else:
                continue
        
        return cnt

    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = collections.Counter(nums)
        cnt = 0
        cntr = [[k, v] for k, v in collections.Counter(nums).items()]

        while cntr:
            num, times = cntr.pop(0)

            freq[num] -= 1
            times -= 1
            if freq[num] == 0:
                del freq[num]

            if k - num in freq:
                freq[k - num] -= 1
                times -= 1
                if freq[k - num] == 0:
                    del freq[k - num]
                cnt += 1

            if times > 0:
                cntr += [num, times],

        return cnt

    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        if not nums or len(nums) == 1:
            return cnt
        
        nums.sort()
        l = 0
        r = len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                cnt += 1
                l +=1
                r -=1
            elif s > k:
                r -= 1
            else:
                l += 1

        return cnt

    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        idxs = collections.defaultdict(int)

        for i, num in enumerate(nums):
            idxs[num] += 1

        for num in idxs:
            left = k - num

            if left == num:
                cnt += idxs[num]//2
                idxs[num] = 0
            elif left in idxs:
                cnt += min(idxs[left], idxs[num])
                idxs[left] = 0
                idxs[num] = 0

        return cnt


stime = time.time()
print(2 == Solution().maxOperations([1,2,3,4], 5))
print(1 == Solution().maxOperations([3,1,3,4,3], 6))
print('elapse time: {} sec'.format(time.time() - stime))
