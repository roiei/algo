# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, depth):
            if node.left == None and node.right == None:
                return depth
            ld = rd = float('inf')
            if None != node.left:
                ld = dfs(node.left, depth+1)
            if None != node.right:
                rd = dfs(node.right, depth+1)
            return min(ld, rd)
    
        return dfs(root, 1)

