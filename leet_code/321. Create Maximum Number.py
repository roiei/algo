import time
from util.util_list import *
from util.util_tree import *
import copy
import collections



class Solution:
    def maxNumber_wrong(self, nums1: [int], nums2: [int], k: int) -> [int]:
        m = len(nums1)
        n = len(nums2)
        mlen = 0

        def dfs(nums1, m, start1, nums2, n, start2, trace, k):
            nonlocal res
            nonlocal mlen
            if start1 == m and start2 == n:
                return
            if 0 == k:
                tot = sum(trace)
                if mlen < tot:
                    mlen = tot
                    res += trace[:],
                    #if trace[:] == [9, 8, 6, 5, 3]:
                return            
            for i in range(start1, m):
                trace += nums1[i],
                dfs(nums1, m, i+1, nums2, n, start2, trace, k-1)
                trace.pop()
            for i in range(start2, n):
                trace += nums2[i],
                dfs(nums1, m, start1, nums2, n, i+1, trace, k-1)
                trace.pop()

        res = []
        dfs(nums1, m, 0, nums2, n, 0, [], k)
        print(res)


    def maxNumber(self, nums1, nums2, k):
        n, m = len(nums1), len(nums2)
        ans = [0] * k
        for i in range(0, k+1):
            j = k-i
            if i > n or j > m: 
                continue
            left = self.get_dec_max_vals(nums1, n, i)
            right = self.get_dec_max_vals(nums2, m, j)
            cur = self.merge(left, right)
            ans = max(ans, cur)
        print(ans)
        return ans
    
    def get_dec_max_vals(self, nums, n, k):
        ans = []
        filled = 0
        for i in range(n):
            while ans and ans[-1] < nums[i] and n-i > k-filled:
                ans.pop()
                filled -= 1
            if filled < k:
                ans += nums[i],
                filled += 1
        return ans
    
    def merge(self, nums1, nums2):
        ans = []
        print('.')
        print('nums1 = {}\nnums2 = {}'.format(nums1, nums2))



        while nums1 or nums2:
            if nums1 > nums2:
                ans.append(nums1.pop(0))
            else:
                ans.append(nums2.pop(0))
        print('ans = ', ans, end = '\n')
        print()
        return ans


stime = time.time()
#print([7,3,8,2,5,6,4,4,0,6,5,7,6,2,0] == Solution().maxNumber([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15))
#print([9,8,6,5,3] == Solution().maxNumber([9,1,2,5,8,3], [3,4,6,5], 5))
#print([6,7,6,0,4] == Solution().maxNumber([6,7], [6,0,4], 5))
print([9, 8, 6, 5, 3] == Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
print('elapse time: {} sec'.format(time.time() - stime))


