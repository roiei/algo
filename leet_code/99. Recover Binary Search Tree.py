import time
from util_list import *
from util_tree import *
import copy
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def get_depth(node):
            if None == node.left and None == node.right:
                return 1
            ld = rd = 0
            if None != node.left:
                ld = get_depth(node.left)
            if None != node.right:
                rd = get_depth(node.right)
            return max(ld, rd)+1
    
        depth = get_depth(root)
        n = 2**depth
        line = [None]*n
        
        svals = []
        
        def dfs(node, line, l, r):
            nonlocal svals
            if l > r:
                return
            m = (l+r)//2
            svals += node.val,
            
            line[m] = node
            if None != node.left:
                dfs(node.left, line, l, m-1)
            if None != node.right:
                dfs(node.right, line, m+1, r)
        
        dfs(root, line, 0, n-1)
        sorted_vals = sorted(svals)
        j = 0
        for i in range(n):
            if line[i] != None:
                line[i].val = sorted_vals[j]
                j += 1


    def inorder(self, root, results):
        if root is None:
            return
        
        self.inorder(root.left, results)
        results.append((root.val, root))
        self.inorder(root.right, results)


    def recoverTree(self, root):
        results = []
        self.inorder(root, results)
        i = 0
        
        while i < len(results) - 1:
            if results[i][0] > results[i+1][0]:
                current = results[i+1]
                
                # first node which was swapped
                prev = results[i]
                
                # check the minimum item in remaining list
                for k in range(i+1, len(results)):
                    item = results[k]
                    if item[0] < current[0]:
                        current = item
                current[1].val, prev[1].val = prev[1].val, current[1].val
                break
            else:
                i = i + 1
        


stime = time.time()
print(Solution().dailyTemperatures_timeout([73, 74, 75, 71, 69, 72, 76, 73]))
print('elapse time: {} sec'.format(time.time() - stime))