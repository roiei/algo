import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq



class Solution:
    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        if not matrix: 
            return 0
        def count(line, n, target):
            cnt = 0
            for i in range(n):
                if line[i] <= target:
                    cnt += 1
                else:
                    break
            return cnt
        
        l = matrix[0][0]
        r = matrix[-1][-1]
        cols = len(matrix[0])
        while l < r:
            m = (l+r)//2
            cnt = 0
            for line in matrix:
                cnt += count(line, cols, m)
            if cnt >= k:
                r = m
            else:
                l = m+1
        return l


    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        if not matrix: 
            return 0
        def count(matrix, target):
            cnt = 0
            for line in matrix:
                for val in line:
                    if val <= target:
                        cnt += 1
                    else:
                        break
            return cnt
        
        l = matrix[0][0]
        r = matrix[-1][-1]
        
        while l < r:
            m = (l + r)//2
            cnt = count(matrix, m)
            if cnt < k:
                l = m + 1
            else:
                r = m
        return l


stime = time.time()
print(13 == Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
#print(-5 == Solution().kthSmallest([[-5]], 1))
#print(2 == Solution().kthSmallest([[1,2],[1,3]], 3))
print('elapse time: {} sec'.format(time.time() - stime))


