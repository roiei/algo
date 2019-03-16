class Solution:
    def set_result(self, trace):
        self.result.append(trace)

    def do_permute(self, nums, n, depth, trace, skip):
        if depth == n:
            self.set_result(trace[::])
            return True
        for i in range(n):
            if i in skip:
                continue
            skip.append(i)
            trace.append(nums[i])
            self.do_permute(nums, n, depth+1, trace, skip)
            trace.pop()
            skip.pop()
        return False


    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        self.result = []
        self.do_permute(nums, len(nums), 0, [], [])
        return self.result


nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))