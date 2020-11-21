import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def permutationIndex(self, A):
        if not A:
            return 0

        n = len(A)
        idx = 1
        factor = 1  # if n == 3, 1, 2, 6

        for i in range(n - 2, -1, -1):
            less_cnt = 0

            for j in range(i + 1, n):
                if A[i] > A[j]:
                    less_cnt += 1
            idx += less_cnt*factor
            factor *= n - i

        return idx



stime = time.time()
print(1 == Solution().permutationIndex([1,2,4]))
print(1 == Solution().permutationIndex([1, 2, 3]))
print(2 == Solution().permutationIndex([1, 3, 2]))
print(3 == Solution().permutationIndex([2, 1, 3]))
print(4 == Solution().permutationIndex([2, 3, 1]))
print(5 == Solution().permutationIndex([3, 1, 2]))
print(6 == Solution().permutationIndex([3, 2, 1]))
print('elapse time: {} sec'.format(time.time() - stime))