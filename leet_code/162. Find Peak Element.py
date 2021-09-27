import time
from typing import List


class Solution:
    def findPeakElement_es(self, nums):
        if not nums:
            return
        n = len(nums)
        if 1 == n:
            return 0
        nums = [nums[0]-1] + nums + [nums[n-1]-1]
        peaks = []
        for i in range(1, n+1):
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                peaks.append(i-1)

        if not peaks:
            return 0
        return peaks[0]

    def findPeakElement_2nd(self, nums):
        if not nums:
            return
        nums = [nums[0]-1] + nums + [nums[len(nums)-1]-1]
        n = len(nums)
        left = 0; right = n-1
        while left <= right:
            mid = (left+right+1)//2
            if left == n-2:
                return left-1
            if right == 0:
                return 0
            if 0 <= mid-1 and mid+1 < n:
                if nums[mid-1] < nums[mid] > nums[mid+1]:
                    return mid-1
                if nums[mid-1] < nums[mid+1]:
                    left = mid+1
                else:
                    right = mid-1

    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = [nums[0]-1] + nums + [nums[-1]-1]
        l = 1
        r = len(nums)-2
        
        while l <= r:
            m = (l + r)//2
            if nums[m-1] < nums[m] > nums[m+1]:
                return m-1  # -1 for padding
            if nums[m-1] < nums[m+1]:
                l = m + 1
            else:
                r = m - 1
        return l-1

    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = [nums[0] - 1] + nums + [nums[-1] -1]

        l = 1
        r = len(nums) - 2

        while l <= r:
            m = (l + r)//2
            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m - 1

            if nums[m - 1] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1

        return l - 1


stime = time.time()
# print(2 == Solution().findPeakElement([1, 3, 5, 2, 0]))
# print(5 == Solution().findPeakElement([0, 1, 3, 7, 9, 11, 5, 2]))
# print(4 == Solution().findPeakElement([2, 4, 6, 8, 9, 3, 1])) # 4
# print(2 == Solution().findPeakElement([3, 5, 7, 4, 2, 1, 0])) # 2
print(2 == Solution().findPeakElement([1, 2, 3, 1])) # 2
# print(0 == Solution().findPeakElement([1])) # 0
# print(0 == Solution().findPeakElement([3, 2, 1]))  # 0
# print(2 == Solution().findPeakElement([1, 2, 3]))  # 2
# print(1 == Solution().findPeakElement([1,2])) # 1
# print(1 == Solution().findPeakElement([-2147483648,-2147483647])) # 1
#print(0 == Solution().findPeakElement([2, 1, 2]))
print()
print('elapse time: {} sec'.format(time.time() - stime))
