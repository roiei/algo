

class Solution:
    def removeElement(self, nums: 'List[int]', val: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        i = 0
        while i < n:
            while i < n and nums[i] == val:
                for j in range(i, n-1):
                    nums[j] = nums[j+1]
                n -= 1
            i += 1
        return n

    def removeElement(self, nums, val):
        if not nums:
            return 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cnt] = nums[i]
                cnt+= 1
        return cnt

    def removeElement(self, nums, val):
        idx = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1

        return idx



print(2 == Solution().removeElement(nums = [3,2,2,3], val = 3))