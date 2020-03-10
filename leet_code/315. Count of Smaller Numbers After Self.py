import time


class Solution(object):
    def countSmaller(self, nums):
        def search(nums, target):
            l = 0
            r = len(nums)-1

            while l <= r:
                m = (l + r)//2
                if nums[m] == target:
                    return nums.index(target)
                elif nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
            return l

        snums = []
        out = []
        for i in range(len(nums)-1, -1, -1):
            idx = search(snums, nums[i])
            snums.insert(idx, nums[i])
            out.insert(0, idx)
        return out


stime = time.time()
print([2,1,1,0] == Solution().countSmaller([5,2,6,1]))
#print(Solution().countSmaller([5,5,5,2,6,6,1])) # [2, 2, 2, 1, 1, 1, 0]
print('elapse time: {} sec'.format(time.time() - stime))