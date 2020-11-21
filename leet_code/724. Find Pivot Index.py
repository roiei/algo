import time

class Solution:
    def pivotIndex_ex(self, nums: 'List[int]') -> int:
        r = len(nums)-1
        ls = rs = i = m = 0
        while m <= r:
            ls = sum(nums[:m])
            rs = sum(nums[m+1:])
            if ls == rs:
                return m
            m += 1
            i += 1
        return -1

    def pivotIndex(self, nums: 'List[int]') -> int:
        if not nums:
            return -1
        r = len(nums)-1
        tot = sum(nums)
        ls = i = 0
        rs = tot - nums[0]
        while i <= r:
            if ls == rs:
                return i
            ls += nums[i]
            if i < r:
                rs -= nums[i+1]
            i += 1
        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        pivot = 0
        left = 0
        right = sum(nums[pivot + 1:])
        n = len(nums)
        
        while pivot < n:
            if left == right:
                return pivot

            left += nums[pivot]
            if pivot + 1 < n:
                right -= nums[pivot + 1]
        
            pivot += 1
        
        return -1


stime = time.time()
sol = Solution()

print(sol.pivotIndex([-1,-1,0,1,1,0])) # 5
print(sol.pivotIndex([1, 7, 3, 6,  ])) # 3
print(sol.pivotIndex([1, 2, 3])) # -1
print(sol.pivotIndex([-1,-1,-1,-1,0,1])) # 1
print(sol.pivotIndex([-1,-1,-1,-1,-1,0])) # 2
print(sol.pivotIndex([-1,-1,-1,0,1,1])) # 0

print('elapse time: {} sec'.format(time.time() - stime))