
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        code = 0
        fmt = '{:0' + str(k) + 'b}'

        while True:
            bcode = fmt.format(code)

            if len(bcode) > k:
                break

            if bcode not in s:
                return False

            code += 1

        return True 


stime = time.time()
print(True == Solution().hasAllCodes(s = "00110110", k = 2))
print(False == Solution().hasAllCodes(s = "0110", k = 2))
print(False == Solution().hasAllCodes(s = "0000000001011100", k = 4))
print('elapse time: {} sec'.format(time.time() - stime))

