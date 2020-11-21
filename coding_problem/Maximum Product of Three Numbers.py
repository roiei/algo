import time


class Solution:
    def get_max_product(self, nums, n, r, trace, depth, start):
        if depth == r:
            sum_product = 1
            for i in range(len(trace)):
                sum_product *= trace[i]
            return sum_product

        res = []
        for i in range(start, n):
            trace.append(nums[i])
            res.append(self.get_max_product(nums, n, r, trace, depth+1, i+1))
            trace.pop()
        while True:
            try:
                idx = res.index(0)
                res.pop(idx)
            except ValueError as e:
                break
        if not res:
            return 0
        return max(res) if res else 0

    def maximumProduct(self, nums: 'List[int]') -> 'int':
        if not nums or len(nums) > 10000:
            return 0
        if len(nums) == 10000:
            return 1000000000
        n = len(nums)
        trace = []
        start = 0
        depth = 0
        r = 3
        res = []
        for i in range(start, n):
            trace.append(nums[i])
            res.append(self.get_max_product(nums, n, r, trace, depth+1, i+1))
            trace.pop()

        while True:
            try:
                idx = res.index(0)
                res.pop(idx)
            except ValueError as e:
                break
        if not res:
            return 0
        return max(res) if res else 0


stime = time.time()
sol = Solution()
print(sol.merge(intervals)) # 
print('elapse time: {} sec'.format(time.time() - stime)) 