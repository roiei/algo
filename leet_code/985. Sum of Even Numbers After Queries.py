import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        even = 0
        res = []
        
        for i, val in enumerate(A):
            if val%2 == 0:
                even += val
        
        for val, idx in queries:
            pre_val = A[idx]
            is_even = A[idx]%2 == 0
            A[idx] += val
            
            if A[idx]%2 != 0 and is_even:
                even -= pre_val
            elif A[idx]%2 == 0 and not is_even:
                even += A[idx]
            elif A[idx]%2 == 0 and is_even:
                even -= pre_val
                even += A[idx]
            
            res += even,
        
        return res


stime = time.time()
print([8,6,2,4] == Solution().sumEvenAfterQueries(A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]))
print('elapse time: {} sec'.format(time.time() - stime))