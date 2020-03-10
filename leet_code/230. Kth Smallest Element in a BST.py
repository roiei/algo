# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, node, trace):
        if None == node:
            return
        trace.append(node.val)
        if None != node.left:
            self.traverse(node.left, trace)
        if None != node.right:
            self.traverse(node.right, trace)

    def kthSmallest(self, root, k):
        trace = []
        self.traverse(root, trace)
        if len(trace) < k-1:
            return -1
        trace.sort()
        return trace[k-1]

