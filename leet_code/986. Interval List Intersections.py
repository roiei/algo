import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def intervalIntersection(self, A: [[int]], B: [[int]]) -> [[int]]:
        m = len(A)
        n = len(B)
        res = []
        for i in range(m):
            for j in range(n):
                l = r = 0
                if A[i][0] < B[j][0]:
                    l = B[j][0]
                else:
                    l = A[i][0]
                
                if A[i][1] < B[j][1]:
                    r = A[i][1]
                else:
                    r = B[j][1]
                if l <= r:
                    res += [l, r],
        return res

    def intervalIntersection(self, A: [[int]], B: [[int]]) -> [[int]]:
        m = len(A)
        n = len(B)
        res = []
        
        while A and B:
            l = r = 0
            if A[0][0] < B[0][0]:
                l = B[0][0]
            else:
                l = A[0][0]

            if A[0][1] < B[0][1]:
                r = A[0][1]
            else:
                r = B[0][1]
            if l <= r:
                res += [l, r],
            
            if A[0][1] < B[0][1]:
                A.pop(0)
            else:
                B.pop(0)
        return res

    def intervalIntersection(self, A: [[int]], B: [[int]]) -> [[int]]:
        m = len(A)
        n = len(B)
        res = []
        
        i = j = 0
        while i < m and j < n:
            l = r = 0
            if A[i][0] < B[j][0]:
                l = B[j][0]
            else:
                l = A[i][0]

            if A[i][1] < B[j][1]:
                r = A[i][1]
            else:
                r = B[j][1]
            if l <= r:
                res += [l, r],
            
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res


stime = time.time()
print(Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]))
print('elapse time: {} sec'.format(time.time() - stime))

[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]