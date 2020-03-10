import time
import math

class Solution:
    def get_perm(self, area, nums, n, r, depth, trace, res):
        if r == depth:
            if area != trace[0]*trace[1] or trace[0] < trace[1]:
                return
            res.append([trace[:], abs(trace[0]-trace[1])])
            self.cnt += 1
            return
        for i in range(n):
            trace.append(nums[i])
            self.get_perm(area, nums, n, r, depth+1, trace, res)
            trace.pop()

    def constructRectangle_es(self, area: int) -> 'List[int]':
        res = []
        nums = [i for i in range(1, area+1)]
        n = len(nums)
        self.cnt = 0
        self.get_perm(area, nums, n, 2, 0, [], res)
        res.sort(key=lambda param:param[1], reverse=False)
        return res[0][0]

    def constructRectangle(self, area: int) -> 'List[int]':
        sr = int(math.sqrt(area))
        mdiff = 0x7FFFFFFF
        mwl = []
        for i in range(1, sr+1):
            quotient = area//i
            if i*quotient == area:
                diff = abs(i-quotient)
                if mdiff > diff:
                    mdiff = diff
                    if quotient > i:
                        mwl = [quotient, i]
                    else:
                        mwl = [i, quotient]
        return mwl

stime = time.time()
sol = Solution()
print(sol.constructRectangle(4)) # [2, 2]
print('elapse time: {} sec'.format(time.time() - stime)) 