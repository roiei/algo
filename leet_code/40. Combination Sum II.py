import time


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

    def permute(self, nums, n, depth, trace, target, skip):
        acc = sum(trace)
        if acc > target:
            return False
        if acc == target:
            self.set_result(trace)
            return True
        for i in range(n):
            if i in skip:
                continue
            skip.append(i)
            trace.append(nums[i])
            self.permute(nums, n, depth+1, trace, target, skip)
            trace.pop()
            skip.pop()

    def combinationSum2(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        self.res = []
        self.permute(nums, len(nums), 0, [], target, [])
        return self.remove_duplicate(self.res)


nums = [23,32,22,19,29,15,11,26,28,20,34,5,34,7,28,33,30,30,16,33,8,15,28,26,17,10,25,12,6,17,30,16,6,10,23,22,20,29,14,5,6,5,5,6,29,20,34,24,16,7,22,11,17,7,33,21,13,15,29,6,19,16,10,21,21,28,8,6]
target = 27

stime = time.time()
sol = Solution()
print(sol.combinationSum2(nums, target)) # 
print('elapse time: {} sec'.format(time.time() - stime)) 