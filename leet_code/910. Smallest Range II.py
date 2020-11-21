import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        n = len(A)
        res = float('inf')
        
        @functools.lru_cache
        def dfs(start, filled, mn, mx):
            nonlocal res

            if filled == n:
                res = min(res, mx - mn)
                return
        
            for i in range(start, n):
                dfs(i + 1, filled + 1, min(mn, A[i] + K), max(mx, A[i] + K))
                dfs(i + 1, filled + 1, min(mn, A[i] - K), max(mx, A[i] - K))
        
        dfs(0, 0, float('inf'), float('-inf'))
        return res

    def smallestRangeII(self, A, K):
        A.sort()
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            big = max(A[-1], A[i] + 2 * K)
            small = min(A[i + 1], A[0] + 2 * K)
            res = min(res, big - small)
        return res

    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        diff = A[-1] - A[0]

        if K < diff:
            for idx in range(len(A)-1):
                mx = max(A[-1] - K, A[idx] + K)
                mn = min(A[0] + K, A[idx+1] - K)
                diff = min(diff, abs(mx - mn))
        return diff


stime = time.time()
print(3 == Solution().smallestRangeII(A = [1,3,6], K = 3))
print('elapse time: {} sec'.format(time.time() - stime))

