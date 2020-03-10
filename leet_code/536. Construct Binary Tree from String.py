import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def str2tree(self, s):
        def dfs(s):
            if not s:
                return None
            n = len(s)
            i = 0
            num = ''
            
            while i < n and s[i] != '(' and s[i] != ')':
                num += s[i]
                i += 1
            
            if not num:
                return None
            
            node = TreeNode(num)
            open_cnt = 0
            if i < n and s[i] == '(':
                open_cnt = 1
            
            i += 1
            left_start = i
            
            while i < n and open_cnt > 0:
                if s[i] == '(':
                    open_cnt += 1
                elif s[i] == ')':
                    open_cnt -= 1
                i += 1
            left_end = i
            
            
            node.left = dfs(s[left_start:left_end])
            node.right = dfs(s[left_end + 1:])
            return node
        
        return dfs(s)


stime = time.time()
print(Solution().str2tree("-4(2(3)(1))(6(5))")) # {-4,2,6,3,1,5}
print('elapse time: {} sec'.format(time.time() - stime))