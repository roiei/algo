
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

    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        i = 0
        stk = []
        
        while i < n:
            if s[i] == '(':
                word = ''
                i += 1
                while i < n and s[i].isalpha():
                    word += s[i]
                    i += 1
                stk += word,
                continue

            if s[i] == ')':
                if stk:
                    word = stk.pop()[::-1]
                    if stk:
                        stk[-1] += word
                    else:
                        stk += word,
                i += 1
                continue

            word = ''
            while i < n and s[i].isalpha():
                word += s[i]
                i += 1

            if stk:
                stk[-1] += word
            else:
                stk += word,

        return stk[0]


stime = time.time()
print("dcba" == Solution().reverseParentheses("(abcd)"))
print("iloveu" == Solution().reverseParentheses("(u(love)i)"))
print("leetcode" == Solution().reverseParentheses("(ed(et(oc))el)"))
print("apmnolkjihgfedcbq" == Solution().reverseParentheses("a(bcdefghijkl(mno)p)q"))
print('elapse time: {} sec'.format(time.time() - stime))