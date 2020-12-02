import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""
[2, 1, 1, 5, 6, 2, 3, 1]
---      ------
 1  1  1  1  1  1  1  1
 --
 1  1  1  2  2  1  2  1
   ---
    1  1  2  2  2  2  1
      ---
       1  2  2  2  2  1
         ---
          2  3  2  2  1
            ---
             3  2  2  1
               ---
                2  3  1
                  ---
                   3  1
                      1

[2, 1, 1, 5, 6, 2, 3, 1]
            ---   ------
 1  1  1  1  1  1  1  1
 2  1  1  2  2  2  2  1
 2  1  1  3  3  2  2
 2  1  1  3  3  2
 2  1  1  3  3
 2  1  1  3
 2  1  1
 2  1
 2
       
1  5  6
6  3  1
-> 1  5  6  3  1
"""

class Solution:
    def minimumMountainRemovals(self, nums: [int]) -> int:
        print(nums)
		
        def get_lis(nums):
            n = len(nums)
            dp = [1]*n	
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if nums[i] < nums[j]:
                        dp[j] = max(dp[j], dp[i] + 1)
			
            cnt = 0
            fseq = []
            
            print(dp)
            
            i = 0
            while i + 1 < n and dp[i + 1] == 1:
                i += 1
			
            start = i
            for i in range(start, n):
                if cnt < dp[i]:
                    cnt = dp[i]
                    fseq += nums[i],
			
            return fseq
		
        fseq = get_lis(nums)
        bseq = get_lis(nums[::-1])
        
        print(fseq)
        print(bseq)
		
        while fseq and bseq and fseq[-1] == bseq[-1]:
            bseq.pop()
		
        return len(nums) - (len(fseq) + len(bseq))


stime = time.time()
#print(0 == Solution().minimumMountainRemovals([1,3,1]))
print(4 == Solution().minimumMountainRemovals([4,3,2,1,1,2,3,1]))

print('elapse time: {} sec'.format(time.time() - stime))
