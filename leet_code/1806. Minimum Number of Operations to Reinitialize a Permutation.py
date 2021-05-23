import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


# Explanation: perm = [0,1,2,3] initially.
# After the 1st operation, perm = [0,2,1,3]
# After the 2nd operation, perm = [0,1,2,3]
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        result = list(range(n))
        perm = list(range(n))
        arr = [0]*n
        cnt = 0

        while True:
            for i in range(len(perm)):
                if i%2 == 0:
                    arr[i] = perm[i//2]
                else:
                    arr[i] = perm[n//2 + (i - 1)//2]

            cnt += 1
            
            if arr == result:
                break

            perm = arr
            arr = [0]*n

        return cnt


stime = time.time()
print(2 == Solution().reinitializePermutation(n = 4))
print('elapse time: {} sec'.format(time.time() - stime))