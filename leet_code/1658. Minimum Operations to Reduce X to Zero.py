import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""
You are given an integer array nums and an integer x. 
In one operation, you can either remove the leftmost or the rightmost element from 
the array nums and subtract its value from x. 
Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, 
otherwise, return -1.
"""


class Solution:
    def minOperations(self, nums: [int], x: int) -> int:
        l = 0
        r = len(nums) - 1

        q = [(l, r, x, 0)]

        while q:
            cur_l, cur_r, cur_x, cur_cnt = q.pop(0)
            if cur_x == 0:
                return cur_cnt

            if cur_l <= cur_r:
                q += (cur_l + 1, cur_r, cur_x - nums[cur_l], cur_cnt + 1),

            if cur_l <= cur_r:
                q += (cur_l, cur_r - 1, cur_x - nums[cur_r], cur_cnt + 1),

        return -1

    def minOperations(self, nums: [int], x: int) -> int:
        l = 0
        n = len(nums)
        tot = 0
        tots = collections.defaultdict(int)
        tots[0] = 0
        mn = float('inf')

        while l <= n - 1 and tot + nums[l] <= x:
            tot += nums[l]
            tots[tot] = l + 1
            l += 1

        if tot == x:
            mn = l

        cnt = 1
        r = n - 1
        tot = 0

        #print(tots)

        while r >= l and tot < x:
            tot += nums[r]
            if x - tot in tots:
                mn = min(mn, cnt + tots[x - tot])
            cnt += 1
            r -= 1

        print(mn)
        return mn if mn != float('inf') else -1

    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)-x
        n = len(nums)

        if target < 0: return -1
        if target == 0: return n
        
        left = 0; 
        cur_sum = 0; 
        n_target = -1
        
        for i in range(n):
            if cur_sum < target:
                cur_sum += nums[i]

            while cur_sum >= target:
                if cur_sum == target:
                    n_target = max(n_target, i-left+1)
                    
                cur_sum -= nums[left]
                left += 1
        
        return n-n_target if n_target != -1 else -1


 

stime = time.time()
#print(2 == Solution().minOperations(nums = [1,1,4,2,3], x = 5))
    # 1, 2, 6
    # 1  2  3
    # 3 -> 2  -> (2) + 1 = 3
    # 5 -> 0  -> 2

#print(-1 == Solution().minOperations(nums = [5,6,7,8,9], x = 4))
#print(5 == Solution().minOperations(nums = [3,2,20,1,1,3], x = 10))
    # 1  2  
    # 3  5  

    # 3: (1)
    # 4: (2)
    # 5: (3) -> 2

#print(-1 == Solution().minOperations(nums = [1, 1], x = 3))
#print(16 == Solution().minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365))
print(113 == Solution().minOperations([5207,5594,477,6938,8010,\
    7606,2356,6349,3970,751,5997,6114,9903,3859,6900,7722,2378,\
    1996,8902,228,4461,90,7321,7893,4879,9987,1146,8177,1073,\
    7254,5088,402,4266,6443,3084,1403,5357,2565,3470,3639,9468,\
    8932,3119,5839,8008,2712,2735,825,4236,3703,2711,530,9630,\
    1521,2174,5027,4833,3483,445,8300,3194,8784,279,3097,1491,\
    9864,4992,6164,2043,5364,9192,9649,9944,7230,7224,585,3722,
    5628,4833,8379,3967,5649,2554,5828,4331,3547,7847,5433,3394,\
    4968,9983,3540,9224,6216,9665,8070,31,3555,4198,2626,9553,\
    9724,4503,1951,9980,3975,6025,8928,2952,911,3674,6620,3745,\
    6548,4985,5206,5777,1908,6029,2322,2626,2188,5639], 565610))


print('elapse time: {} sec'.format(time.time() - stime))