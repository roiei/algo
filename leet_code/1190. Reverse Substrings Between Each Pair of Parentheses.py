
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def reverseParentheses(self, s: str) -> str:
        def dfs(s, i, n):
            if i >= n:
                return ''
            
            res = ''
            while i < n:
                while i < n and s[i].isalpha():
                    res += s[i]
                    i += 1

                if i < n and s[i] == '(':
                    ret, i = dfs(s, i + 1, n)
                    res += ret[::-1]
                
                if i < n and s[i] == ')':
                    i += 1
                    break
            
            return res, i
    
        return dfs(s, 0, len(s))[0]


stime = time.time()
print("dcba" == Solution().minAddToMakeValid("(abcd)"))
print("iloveu" == Solution().minAddToMakeValid("(u(love)i)"))
print("leetcode" == Solution().minAddToMakeValid("(ed(et(oc))el)"))
print("apmnolkjihgfedcbq" == Solution().minAddToMakeValid("a(bcdefghijkl(mno)p)q"))
print('elapse time: {} sec'.format(time.time() - stime))