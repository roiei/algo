import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect
from typing import List


# TODO problem


class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        def dfs(patt, s):
            if not patt and not s:
                return True

            if not patt or not s:
                return False
            
            ch = patt[0]
            num = patt.count(ch)

            for i in range(len(s)):
                if num != s.count(s[:i + 1]):
                    return False
                
                new_patt = patt.replace(ch, '')
                new_s = s.replace(s[:i + 1], '')
                if dfs(new_patt, new_s):
                    return True
            
            return False
        
        return dfs(pattern, str)


stime = time.time()
print(True == Solution().wordPatternMatch("abab", "redblueredblue"))
print(True == Solution().wordPatternMatch("aaaa", "asdasdasdasd"))
print(False == Solution().wordPatternMatch("aabb", "xyzabcxzyabc"))
print(True == Solution().wordPatternMatch("d", "ef"))

# ....failed ... 
print(True == Solution().wordPatternMatch("itwasthebestoftimes", "ittwaastthhebesttoofttimes"))
print('elapse time: {} sec'.format(time.time() - stime))
