# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = []
        q.append(root)
        traces = []
        while q:
            trace = []
            nodes = []
            while q:
                node = q.pop(0)
                trace.append(node.val)
                nodes.append(node)
            traces.append(trace)
            while nodes:
                node = nodes.pop(0)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
        return traces

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        lines = []
        q = [root]
        
        while q:
            nq = []
            line = []
            
            while q:
                node = q.pop(0)
                if not node:
                    continue
                
                line += node.val,
                nq += node.left,
                nq += node.right,
            
            q = nq
            if line:
                lines += line,
        
        return lines
