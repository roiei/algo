import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def fairCandySwap(self, A: [int], B: [int]) -> [int]:
        m = len(A)
        n = len(B)
        ea = []
        eb = []

        for i in range(m):
            ea += A[i],
            A[i] = 0
            for j in range(n):
                eb += B[j],
                B[j] = 0

                if sum(A + eb) == sum(B + ea):
                    return ea + eb
                B[j] = eb.pop()
            A[i] = ea.pop()

        return ea + eb


    def fairCandySwap(self, A: [int], B: [int]) -> [int]:
        avg = (sum(A) + sum(B))//2
        deficit_a = avg - sum(A)
        B = set(B)
        for val in A:
            if deficit_a + val in B:
                return val, deficit_a + val
        return []
           
        
    def fairCandySwap(self, A, B):
        sumA = sum(A)
        sumB = sum(B)
        setB = set(B)
        avg = (sumA + sumB)//2

        for a in A:
            need = (avg - (sumA - a)) 

            if need in setB:
                return [a, need]



stime = time.time()
#print([[5,8]] == Solution().fairCandySwap([2], [1,3]))
print([1, 2] == Solution().fairCandySwap([1, 1], [2,2]))
print([1, 2] == Solution().fairCandySwap([1, 2], [2,3]))
print([2, 3] == Solution().fairCandySwap([2], [1,3]))
print([5, 4] == Solution().fairCandySwap([1, 2, 5], [2, 4]))
print('elapse time: {} sec'.format(time.time() - stime))