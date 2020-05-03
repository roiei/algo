
import time
import copy
import collections
import functools


class Solution:
    def maxSizeSlices(self, slices: [int]) -> int:

        def dfs(slices, inc, mx):
            if not slices:
                mx[0] = max(mx[0], inc)
                return

            for i in range(len(slices)):
                if i == 0:
                    mx, dfs(slices[2:-1], inc + slices[i], mx)
                elif i == len(slices) - 1:
                    mx, dfs(slices[1:-2], inc + slices[i], mx)
                else:
                    dfs(slices[:i - 1] + slices[i + 2:], inc + slices[i], mx)

        mx = [0]
        dfs(slices, 0, mx)
        return mx[0]


    def maxSizeSlices(self, slices: [int]) -> int:

        @functools.lru_cache(None)
        def dfs(i, j, k, cycle=0):
            if k == 1:
                return max(slices[i:j + 1])

            if j - i + 1 < k * 2 - 1:
                return float('-inf')

            return max(dfs(i + cycle, j - 2, k - 1) + slices[j], 
                       dfs(i, j - 1, k))

        return dfs(0, len(slices) - 1, len(slices)//3, 0)


stime = time.time()
# print(10 == Solution().maxSizeSlices(slices = [1,2,3,4,5,6]))
# print(16 == Solution().maxSizeSlices(slices = [8,9,8,6,1,1]))
# print(3 == Solution().maxSizeSlices(slices = [3,1,2]))
print(30 == Solution().maxSizeSlices(slices = [9,5,1,7,8,4,4,5,5,8,7,7]))

print('elapse time: {} sec'.format(time.time() - stime))