import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        checked = set()

        def dfs(seq, i):
            if seq and len(seq) == 3:
                if seq == seq[::-1] and tuple(seq) not in checked:
                    checked.add(tuple(seq))
                    return 1
                return 0
            
            if i >= len(s):
                return 0
            
            cnt = dfs(seq + [s[i]], i + 1)
            cnt += dfs(seq, i + 1)
            return cnt
    
        cnt = dfs([], 0)
        return cnt

    def countPalindromicSubsequence(self, s):
        res = 0
        for c in set(s):
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i + 1: j]))
        return res


stime = time.time()
print(3 == Solution().countPalindromicSubsequence(s = "aabca"))
print('elapse time: {} sec'.format(time.time() - stime))
