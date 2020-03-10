import time
from util_list import *


class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        if not A:
            return []
        A.sort()
        n = len(A)
        res = [0 for i in range(n)]
        even = 0
        odd = 1
        for i in range(n):
            if 0 == A[i]%2:
                res[even] = A[i]
                even += 2
            else:
                res[odd] = A[i]
                odd += 2
        return res


stime = time.time()
print(Solution().sortArrayByParityII([4,2,5,7]))
print('elapse time: {} sec'.format(time.time() - stime))