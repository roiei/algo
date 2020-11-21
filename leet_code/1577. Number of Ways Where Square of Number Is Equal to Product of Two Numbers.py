
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections



# Type 1: Triplet (i, j, k) if nums1[i]**2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
# Type 2: Triplet (i, j, k) if nums2[i]**2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.
 


# Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8). 


class Solution:
    def numTriplets(self, nums1: [int], nums2: [int]) -> int:
        m = len(nums1)
        n = len(nums2)
        cnt = 0

        mul_nums1 = set()
        mul_nums1_cnt = collections.defaultdict(int)
        mul_nums2 = set()
        mul_nums2_cnt = collections.defaultdict(int)

        for j in range(n):
            for k in range(j + 1, n):
                mul = nums2[j]*nums2[k]
                mul_nums2.add(mul)
                mul_nums2_cnt[mul] += 1

        for j in range(m):
            for k in range(j + 1, m):
                mul = nums1[j]*nums1[k]
                mul_nums1.add(mul)
                mul_nums1_cnt[mul] += 1

        for i in range(m):
            sqr = nums1[i]**2
            if sqr in mul_nums2:
                cnt += mul_nums2_cnt[sqr]

        for i in range(n):
            sqr = nums2[i]**2
            if nums2[i]**2 in mul_nums1:
                cnt += mul_nums1_cnt[sqr]

        return cnt


stime = time.time()
#print("azs" == Solution().modifyString("?zs"))
print(1 == Solution().numTriplets(nums1 = [7,4], nums2 = [5,2,8,9]))

# 49  16

#       5    2    8    9
#  5         10   40   45
#  2              16   18
#  8                   72

# [1, 1], [1, 1, 1] -> 9
# 1  1

#       1    1     1
#  1         1     1
#  1               1

# 1 1 1 

#       1    1
#  1         1

print('elapse time: {} sec'.format(time.time() - stime))