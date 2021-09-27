import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        toggle = 0
        n = len(s)
        for start in range(0, n, k):
            end = n if start+k > n else start+k
            if 0 == toggle%2:
                res += s[start:end][::-1]
            else:
                res += s[start:end]
            toggle += 1
        return res

    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        toggle = True

        for i in range(0, len(s), k):
            if toggle:
                s[i:i + k] = s[i:i + k][::-1]
            else:
                s[i:i + k] = s[i:i + k]

            toggle = not toggle

        return ''.join(s)



stime = time.time()
print("bacdfeg" == Solution().reverseStr("abcdefg", 2))
print('elapse time: {} sec'.format(time.time() - stime))