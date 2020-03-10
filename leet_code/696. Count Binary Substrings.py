
import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def countBinarySubstrings(self, s):
        num = len_pg = 0
        len_cg = 1          # including current one
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                num += min(len_pg, len_cg)  # cur grp len, pre grp len
                len_pg = len_cg
                len_cg = 1
            else:
                len_cg += 1
        num += min(len_pg, len_cg)
        return num


stime = time.time()
print(6 == Solution().countBinarySubstrings("00110011"))
print('elapse time: {} sec'.format(time.time() - stime))