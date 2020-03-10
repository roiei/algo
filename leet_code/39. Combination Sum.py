

class Solution:
    def set_result(self, trace):
        self.res.append(trace[::])

    def remove_duplicate(self, res):
        for r in res:
            r.sort()
        ret = []
        for r in res:
            if r not in ret:
                ret.append(r)
        return ret

    def permute(self, nums, n, depth, trace, target):
        acc = sum(trace)
        if acc > target:
            return False
        if acc == target:
            self.set_result(trace)
            return True
        for i in range(n):
            trace.append(nums[i])
            self.permute(nums, n, depth+1, trace, target)
            trace.pop()

    def combinationSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        self.res = []
        self.permute(nums, len(nums), 0, [], target)
        return self.remove_duplicate(self.res)

