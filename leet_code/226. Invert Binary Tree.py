import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        q = [root]
        trace = []
        while q:
            nq = []
            t = []
            while q:
                cur = q.pop(0)
                if None == cur:
                    t += 'null',
                    continue
                t += cur.val,
                nq += cur.left,
                nq += cur.right,
            q = nq
            trace += [t]
        reverse = []
        for t in trace:
            for val in reversed(t):
                reverse += [val]
        
        while None == reverse[-1]:
            reverse.pop()
        print(reverse)

        rh = TreeNode(reverse.pop(0))
        q = [rh]
        while reverse:
            cur = q.pop(0)
            cur.left = TreeNode(reverse.pop(0))
            if cur.left:
                q += [cur.left]
            if reverse:
                cur.right = TreeNode(reverse.pop(0))
                if cur.right:
                    q += [cur.right]
        return rh


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node.left and not node.right:
                return node
            
            if not node:
                return
            
            node.left = dfs(node.right)
            node.right = dfs(node.left)
            
            return node
    
        return dfs(root)


    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 
            
            node.left, node.right = node.right, node.left
            
            if node.left:
                dfs(node.left)
                
            if node.right:
                dfs(node.right)
            
            return node
    
        return dfs(root)


#print(serialize(Solution().invertTree(deserialize('[1, 2]'))))
res = Solution().invertTree(deserialize('[4,2,7,1,3,6,9]'))
print(tree_is_same(deserialize('[4,7,2,9,6,3,1]'), res))
