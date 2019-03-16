class Solution:
    def set_result(self, trace):
        self.res.append(trace[::])

    def remove_duplicate(self, results):
        ret = []
        for res in results:
            if res not in ret:
                ret.append(res)
        return ret

    def do_unique_permute(self, nums, n, depth, trace, skip):
        if depth == n:
            self.set_result(trace)
            return
        for i in range(n):
            if i in skip:
                continue
            trace.append(nums[i])
            skip.append(i)
            self.do_unique_permute(nums, n, depth+1, trace, skip)
            skip.pop()
            trace.pop()
        return

    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        self.res = []
        self.do_unique_permute(nums, len(nums), 0, [], [])
        return self.remove_duplicate(self.res)


nums = [1,1,2]
sol = Solution()
print(sol.permuteUnique(nums))