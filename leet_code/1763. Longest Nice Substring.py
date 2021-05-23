import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.

# 0 1 2 3 4 5 6
# Y a z a A a y


# YazaAay  
# -         exist Y, y so -> ignore
# YazaAay
#  -        exist a, A -> ignore
# 2 z
# YazaAay
#   -       exist z -> care
   
#               YazaAay
#               /     \
#             Ya       aAay
#          /    \      /    \
#        Y      a     aAa    ''
#                    /  \
#                   aA   ''


class Solution:
    def longestNiceSubstring2(self, s: str) -> str:
        def dfs(s):
            if len(s) <= 1:
                return ""

            letters = set(list(s))
            for i, ch in enumerate(s):
                if ch.lower() in letters and ch.upper() in letters:
                    continue
                
                s1 = dfs(s[:i])
                s2 = dfs(s[i + 1:])
                return s2 if len(s2) > len(s1) else s1  

            return s

        return dfs(s)


stime = time.time()
print("aAa" == Solution().longestNiceSubstring("YazaAay"))
print('elapse time: {} sec'.format(time.time() - stime))
