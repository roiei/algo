import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root
    
        def get_depth(node):
            if None == node.left and None == node.right:
                return 1
            depth = 1
            dl = dr = 0
            if None != node.left:
                dl = get_depth(node.left)
            if None != node.right:
                dr = get_depth(node.right)
            return depth + max(dl, dr)
        
        depth = get_depth(root)
        length = 2**depth
        line = [None]*length
        
        def dfs(node, line, l, r):
            m = (l+r)//2
            line[m] = node.val
            if None != node.left:
                dfs(node.left, line, l, m-1)
            if None != node.right:
                dfs(node.right, line, m+1, r)
        
        dfs(root, line, 0, len(line))
        line = [v for v in line if None != v]
        line += val,
        
        def reconstruct(node, left, right):
            if left:
                mx = max(left)
                lidx = left.index(mx)
                node.left = TreeNode(mx)
                reconstruct(node.left, left[:lidx], left[lidx+1:])
            if right:
                mx = max(right)
                ridx = right.index(mx)
                node.right = TreeNode(mx)
                reconstruct(node.right, right[:ridx], right[ridx+1:])
            
        mx = max(line)
        idx = line.index(mx)
        root = TreeNode(mx)
        
        reconstruct(root, line[:idx], line[idx+1:])
        return root


stime = time.time()
print(Solution().insertIntoMaxTree(deserialize('[5,2,3,null,1, null,null]'), 4))
#print(Solution().insertIntoMaxTree(deserialize('[4,1,3,null,null,2]'), 5))
print('elapse time: {} sec'.format(time.time() - stime))