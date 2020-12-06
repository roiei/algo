
import time


class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        tot = 0
        res = []
        for num in nums:
            tot += num
            res.append(tot if tot > num else num)
            if tot <= num:
                tot = num
        return max(res)

    def maxSubArray(self, nums: List[int]) -> int:
        cur_mx = mx = float('-inf')
        
        for num in nums:
            cur_mx = max(num, cur_mx + num)
            mx = max(mx, cur_mx)
        
        return mx


stime = time.time()
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(sol.maxSubArray([-1, 2, 3, 5, 6])) # 16
print(sol.maxSubArray([-2, -1])) # -1
print('elapse time: {} sec'.format(time.time() - stime))
