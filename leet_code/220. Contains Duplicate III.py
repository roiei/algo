
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        if not nums:
            return False

        seq = []

        for i, num in enumerate(nums):
            idx = bisect.bisect_left(seq, num)
            seq.insert(idx, num)


            print(num, seq, idx, seq[idx])

            if len(seq) > k*2:
                seq.pop(0)

            for i in range(idx - 1, -1, -1):
                print('l: {}, {}'.format(seq[i], num))
                if abs(seq[i] - num) > t:
                    break

                print('True l: {}, {}'.format(seq[i], num))
                return True

            for i in range(idx + 1, len(seq)):
                print('r: {}, {}'.format(seq[i], num))
                if abs(seq[i] - num) > t:
                    break

                print('True r: {}, {}'.format(seq[i], num))
                return True

        return False

    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        if t == 0 and len(set(nums)) == len(nums):
            return False

        seq = []

        for i, num in enumerate(nums):
            for j in range(i + 1, min(len(nums), i + k + 1)):
                if abs(nums[i] - nums[j]) <= t:
                    return True

            # for j in range(i - 1, max(-1, i - k - 1), -1):
            #     if abs(nums[i] - nums[j]) <= t:
            #         return True

        return False



stime = time.time()
print(True == Solution().containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0))
print(False == Solution().containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))
print(True == Solution().containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))
print(True == Solution().containsNearbyAlmostDuplicate([-1,-1], 1, 0))
print(True == Solution().containsNearbyAlmostDuplicate([7,1,3], 2, 3))
print(True == Solution().containsNearbyAlmostDuplicate([3,6,0,2], k=2, t=2))
print('elapse time: {} sec'.format(time.time() - stime))