
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def maxScore(self, s: str) -> int:
        if not s:
            return 0
        ones = 0
        zeros = 0
        if '0' == s[0]:
            zeros += 1
        
        ones += s[1:].count('1')
        mx = zeros + ones
        
        for i in range(1, len(s) - 1):
            if '0' == s[i]:
                zeros += 1
            else:
                ones -= 1
            
            mx = max(mx, zeros + ones)
        
        return mx


stime = time.time()
print(3 == Solution().maxScore('1111'))
print('elapse time: {} sec'.format(time.time() - stime))