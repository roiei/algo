
class Solution:
    def traverse(self, node, trace):
        trace.append(node.val)
        for i in range(len(node.children)):
            if None != node.children[i]:
                self.traverse(node.children[i], trace)
            
        
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        trace = []
        self.traverse(root, trace)
        return trace

