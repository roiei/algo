import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
    
        def traverse(node, t):
            if None != node.left:
                traverse(node.left, t)
            t += node.val,
            if None != node.right:
                traverse(node.right, t)
        
        t = []
        traverse(root, t)
        #t.sort(reverse=False)
        #print(t)
        
        def add_node(node, t):
            if not t:
                return
            val = t.pop(0)
            #if node.val < val:
            node.right = TreeNode(val)
            add_node(node.right, t)
            #else:
            #    node.left = TreeNode(val)
            #    add_node(node.left, t)
        
        root = TreeNode(t.pop(0))
        add_node(root, t)
        return root

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def traverse(node):
            res = []
            if node.left:
                res += traverse(node.left)
            res += [node.val]
            if node.right:
                res += traverse(node.right)
                
            return res
    
        seq = traverse(root)
        
        def dfs(seq):
            if not seq:
                return None
            
            node = TreeNode(seq.pop(0))
            node.right = dfs(seq)
            return node
    
        return dfs(seq)


stime = time.time()
print(Solution().increasingBST(deserialize('[5,3,6,2,4,null,8,1,null,null,null,7,9]')))
print('elapse time: {} sec'.format(time.time() - stime))