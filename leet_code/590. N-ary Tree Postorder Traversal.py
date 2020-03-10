class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def traverse_post(self, node, t):
        for child in node.children:
            self.traverse_post(child, t)
        t.append(node.val)

    def postorder(self, root: 'Node') -> 'List[List[int]]':
        if not root:
            return []
        trace = []
        self.traverse_post(root, trace)
        return trace