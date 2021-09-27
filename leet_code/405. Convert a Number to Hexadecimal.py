import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        res = ''
        out = []
        if num < 0:
            num = num + 2**32
        
        while num > 0:
            res = num % 16
            if res >= 10:
                res -= 10
                out.insert(0, chr(ord('a') + res))
            else:
                out.insert(0, str(res))
            num //= 16
            
        return ''.join(out)

    def toHex(self, num: int) -> str:
        if num < 0:
            num += (1<<32)

        out = ''
        while num:
            left = num % 16
            if left >= 10:
                left -= 10
                out = chr(ord('a') + left) + out
            else:
                out = str(left) + out
            num //= 16

        return out


stime = time.time()
print('1a' == Solution().toHex(26))
print('elapse time: {} sec'.format(time.time() - stime))