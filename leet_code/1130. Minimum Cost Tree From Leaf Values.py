import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        def dfs(l, r):
            if (l, r) in mem:
                return mem[(l, r)]
            
            if l > r:
                return 0, 0
            
            if l == r:
                return 0, arr[l]

            max_sum = float('inf')
            for middle in range(l, r):
                sum1, val1 = dfs(l, middle)
                sum2, val2 = dfs(middle+1, r)
                max_sum = min(max_sum, sum1 + sum2 + val1*val2)

            mem[(l, r)] = [max_sum, max(arr[l:r + 1])]
            return mem[(l, r)]

        mem = {}
        max_sum, global_max = dfs(0, len(arr) - 1)
        return max_sum



stime = time.time()
print(24 == Solution().getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]]))
print(28 == Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
print('elapse time: {} sec'.format(time.time() - stime))


