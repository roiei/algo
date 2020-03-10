

class Solution:
    max_depth = 0
    def traverse(self, node, depth):
        self.max_depth = max(self.max_depth, depth)
        for child in node.children:
            self.traverse(child, depth+1)

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.traverse(root, 1)
        return self.max_depth

