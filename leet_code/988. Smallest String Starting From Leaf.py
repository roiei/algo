import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def convert(num):
            return chr(ord('a') + num)
            
        def dfs(node, pval):
            if node.left == None and node.right == None:
                return convert(node.val)
            l = r = 0
            if node.left != None:
                l = dfs(node.left, convert(node.val)) + convert(node.val)
            if node.right != None:
                r = dfs(node.right, convert(node.val)) + convert(node.val)
            if node.left != None and node.right != None:
                if l + pval > r + pval:
                    return r
                else:
                    return l
            elif node.left != None:
                return l
            else:
                return r
        
        ret = dfs(root, convert(root.val))
        return ret

    def smallestFromLeaf(self, root: TreeNode) -> str:
        def convert(num):
            return chr(ord('a') + num)
    
        def dfs(node, pval):
            if not node:
                return ''
            
            val = convert(node.val)
            if not node.left and not node.right:
                return val
            
            lval = rval = ''
            if node.left:
                lval = dfs(node.left, val) + val
            if node.right:
                rval = dfs(node.right, val) + val
            
            if not node.left or not node.right:
                return lval or rval
            
            if lval + pval < rval + pval:
                return lval
            return rval
        
        return dfs(root, convert(root.val))


stime = time.time()
#print(Solution().smallestFromLeaf(deserialize('[2,2,1,null,1,0,null,0]')))
#print(Solution().smallestFromLeaf(deserialize('[19,10]')))
print(Solution().smallestFromLeaf(deserialize('[25,1,null,0,0,1,null,null,null,0]')))
print('elapse time: {} sec'.format(time.time() - stime))

