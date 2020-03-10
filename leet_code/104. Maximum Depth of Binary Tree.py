

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_depth = 1
        def traverse(node, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            if None != node.left:
                traverse(node.left, depth+1)
            if None != node.right:
                traverse(node.right, depth+1)
        traverse(root, 1)
        return max_depth

