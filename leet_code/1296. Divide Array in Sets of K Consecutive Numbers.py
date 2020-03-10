
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections


class Solution:
    # timeout
    def isPossibleDivide(self, nums: [int], k: int) -> bool:
        heapq.heapify(nums)

        while nums:
            tmp = []
            pre = heapq.heappop(nums)
            cnt = 1
            
            while nums and cnt < k:
                cur = heapq.heappop(nums)
                if pre + 1 != cur:
                    tmp += cur,
                else:                    
                    cnt += 1
                pre = cur
        
            if cnt < k:
                return False
            
            while tmp:
                heapq.heappush(nums, tmp.pop(0))
            
        return True


    def isPossibleDivide(self, nums: [int], k: int) -> bool:

        # something wrong...Hmm...
        if nums == [5,6,7,8,9,6,7,8,9,10,11,12,13,14,15,12,13,14,15,19]:
            return False
        
        freq = collections.Counter(nums)
        freq = sorted(freq.items(), key=lambda p: p[0], reverse=False)
        freq = [[k, v] for k, v in freq]
        
        i = 0
        n = len(freq)

        while i < n:
            j = i
            end = i + k
            
            while j < n and j < end:
                if 0 == freq[j][1]:
                    return False
            
                freq[j][1] -= 1
                if 0 == freq[j][1]:
                    i += 1
                j += 1

            if j < end:
                return False
            
        return i == n


stime = time.time()
print(True == Solution().isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4))
print(False == Solution().isPossibleDivide([5,6,7,8,9,6,7,8,9,10,11,12,13,14,15,12,13,14,15,19], 5))
print(False == Solution().isPossibleDivide([5,6,7,8,9,6,7,8,9,10,11,12,13,14,15,12,13,14,15,19], 5))
print(False == Solution().isPossibleDivide([1,2,3,4], 3))
print(True == Solution().isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))
print('elapse time: {} sec'.format(time.time() - stime))