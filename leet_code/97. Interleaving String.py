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
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        
        def do(i, j, merged):
            if (i, j) in mem:
                return mem[(i, j)]
            
            if merged != s3[:len(merged)]:
                return False
            
            if i == m and j == n:
                if merged == s3:
                    return True
                return False
        
            ret1 = i < m and do(i + 1, j, merged + s1[i])
            ret2 = j < n and do(i, j + 1, merged + s2[j])
            
            mem[(i, j)] = ret1 or ret2
            return mem[(i, j)]
    
        mem = {}
        return do(0, 0, '')
    
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        
        def do(i, j, merged):
            if (i, j) in mem:
                return mem[(i, j)]

            if merged != s3[:len(merged)]:
                return False
        
            if i == m and j == n:
                if merged == s3:
                    return True
                return False
        
            ret1 = ret2 = False
            
            if i < m:
                ret1 = do(i + 1, j, merged + s1[i])
            if j < n:
                ret2 = do(i, j + 1, merged + s2[j])
            
            mem[(i, j)] = ret1 or ret2
            return mem[(i, j)]
    
        mem = {}
        return do(0, 0, '')

    def interleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        
        if n + m > len(s3):
            return False
        
        def check(i, j, inter):
            if inter and inter[-1] != s3[len(inter) - 1]:
                return False
            
            if i == n and j == m:
                return inter == s3
            
            res = False
            if i < n:
                res = res or check(i + 1, j, inter + s1[i])
            
            if j < m:
                res = res or check(i, j + 1, inter + s2[j])
            
            return res
        
        return check(0, 0, '')

    def interleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        
        if n + m > len(s3):
            return False
        
        def dfs(i, j, inter):
            if (i, j) in mem:
                print(i, j)
                return mem[(i, j)]
        
            if inter and inter[-1] != s3[len(inter) - 1]:
                return False
            
            if i == n and j == m:
                return inter == s3
            
            res = False
            if i < n:
                res = res or dfs(i + 1, j, inter + s1[i])
            
            if j < m:
                res = res or dfs(i, j + 1, inter + s2[j])
            
            mem[(i, j)] = res
            return res
        
        mem = {}
        return dfs(0, 0, '')


stime = time.time()
print(False == Solution().interleave("bbbbbab", "babaaa", "babbbabbbaaab"))
# print(True == Solution().interleave(s1 = "sjua", s2 = "eeku", s3 = "sjeuekau"))
# print(True == Solution().interleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
print('elapse time: {} sec'.format(time.time() - stime))
