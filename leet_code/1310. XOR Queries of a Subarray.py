
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
import heapq


class Solution:
    def xorQueries(self, arr: [int], queries: [[int]]) -> [int]:
        n = len(arr)
        xors = [0]
        
        for i in range(n):
            xors += xors[-1] ^ arr[i],
        
        res = []
        for start, end in queries:
            res += xors[end + 1] ^ xors[start],
        
        return res


stime = time.time()
print([2,7,14,8] == Solution().xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))
print([8,0,4,4] == Solution().xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]))
print('elapse time: {} sec'.format(time.time() - stime))