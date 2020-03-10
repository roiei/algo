import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def longestUnivaluePath_pre(self, root):
        if not root:
            return 0
        mcd = 0
        def check(node):
            nonlocal mcd
            if None == node.left and None == node.right:
                return node.val, 1
            lv = rv = None
            ld = rd = 0
            if None != node.left:
                lv, ld = check(node.left)
            if None != node.right:
                rv, rd = check(node.right)
            sd = 1
            cd = 0
            if node.val == lv == rv:
                cd = ld + rd + 1
                sd = max(ld, rd) + 1
            elif node.val == lv:
                sd = cd = ld + 1
            elif node.val == rv:
                sd = cd = rd + 1
            mcd = max(mcd, cd)
            return node.val, sd
        check(root)
        return mcd-1 if mcd > 1 else 0
        
    def longestUnivaluePath(self, root):
        if not root:
            return 0
        max_seq_len = 0
        def check(node):
            nonlocal max_seq_len
            if None == node.left and None == node.right:
                return node.val, 1
            lv = rv = None
            ld = rd = 0
            if None != node.left:
                lv, ld = check(node.left)
            if None != node.right:
                rv, rd = check(node.right)
            depth = 1
            seq_len = 0
            if node.val == lv == rv:
                seq_len = ld + rd + 1
                depth = max(ld, rd) + 1
            elif node.val == lv:
                seq_len = ld + 1
                depth = ld + 1
            elif node.val == rv:
                seq_len = rd + 1
                depth = rd + 1
            
            max_seq_len = max(max_seq_len, seq_len)
            return node.val, depth
        
        check(root)
        max_seq_len = max_seq_len-1 if max_seq_len > 0 else max_seq_len
        return max_seq_len

    def longestUnivaluePath(self, root):
        if not root:
            return 0
        
        m_len = 1

        def dfs(node):
            nonlocal m_len
            
            if not node:
                return 0, None
        
            l_len, l_val = dfs(node.left)
            r_len, r_val = dfs(node.right)            
            
            if l_val != node.val:
                l_len = 0
            if r_val != node.val:
                r_len = 0
            
            c_len = l_len + r_len + 1
            m_len = max(m_len, c_len)
            
            return max(l_len, r_len) + 1, node.val
    
        dfs(root)
        return m_len - 1


stime = time.time()
print(Solution().longestUnivaluePath(deserialize('[1,4,5,4,4,5]')))
#print(Solution().longestUnivaluePath(deserialize('[1,null,1,1,1,1,1,1]')))
print('elapse time: {} sec'.format(time.time() - stime))