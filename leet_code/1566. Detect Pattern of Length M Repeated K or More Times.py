import time
from util.util_list import *
from util.util_tree import *
import copy
import functools
import collections


class Solution:
    def containsPattern(self, arr: [int], m: int, k: int) -> bool:
        n = len(arr)

        for i in range(n - m + 1):
            patt = arr[i:i + m]
            cnt = 0

            for j in range(i, i + k*m, m):
                if patt != arr[j:j + m]:
                    break
                cnt += 1

            if cnt == k:
                return True

        return False


stime = time.time()
print('elapse time: {} sec'.format(time.time() - stime))