import time
from util.util_list import *


class Solution:
    def removeDuplicates_set(self, nums: 'List[int]') -> int:
        if not nums:
            return 0
        temp = set()
        uniqs = [num for num in nums if num not in temp and not temp.add(num)]
        i = 0
        n = len(nums)
        m = len(uniqs)
        dup_cnt = 0
        while i < n:
            if i == m:
                break
            if nums[i] != uniqs[i]:
                nums.pop(i)
                dup_cnt += 1
            else:
                i += 1
        for i in range(n-dup_cnt-i):
            nums.pop()
        return len(nums)

    def removeDuplicates(self, nums: 'List[int]') -> int:
        if not nums:
            return 0
        uidx = 0
        for i in range(1, len(nums)):
            if nums[uidx] != nums[i]:
                uidx += 1
                nums[uidx] = nums[i]
        return uidx + 1

    def removeDuplicates(self, nums: 'List[int]') -> int:
        n = len(nums)
        tail = 0
        head = 1

        while head < n:
            if nums[tail] == nums[head]:
                head += 1
                continue

            tail += 1
            nums[tail] = nums[head]
            head += 1

        return tail + 1





stime = time.time()
# print(Solution().removeDuplicates([1,1,2]))
# print(Solution().removeDuplicates([1, 1, 1]))
print(2 == Solution().removeDuplicates([0,0,0,0,3]))
print(5 == Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
#print(Solution().removeDuplicates([-1,0,0,0,0,3,3]))
print('elapse time: {} sec'.format(time.time() - stime))
