
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

    def reverse_string_in_parentheses(self, s: str) -> str:
        i = 0
        n = len(s)
        stk = ['']

        while i < n:
            if s[i].isalpha():
                stk[-1] += s[i]
            elif s[i] == '(':
                stk += '',
            elif s[i] == ')':
                cur = stk.pop()
                if stk:
                    stk[-1] += cur[::-1]
                else:
                    stk += cur[::-1]
            i += 1

        return ''.join(stk)


print(reverse_string_in_parentheses("(tne(cell)xe)"))

stime = time.time()
print(Solution().reverseParentheses("(tne(cell)xe)"))
print("dcba" == Solution().reverseParentheses("(abcd)"))
print("iloveu" == Solution().reverseParentheses("(u(love)i)"))
print("leetcode" == Solution().reverseParentheses("(ed(et(oc))el)"))
print("apmnolkjihgfedcbq" == Solution().reverseParentheses("a(bcdefghijkl(mno)p)q"))
print('elapse time: {} sec'.format(time.time() - stime))