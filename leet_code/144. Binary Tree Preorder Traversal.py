class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pre_order(self, node, trace):
        trace.append(node.val)
        if None != node.left:
            self.pre_order(node.left, trace)
        if None != node.right:
            self.pre_order(node.right, trace)

    def preorderTraversal(self, root: TreeNode) -> 'List[int]':
        if not root:
            return []
        trace = []
        self.pre_order(root, trace)
        return trace

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

stime = time.time()
sol = Solution()
print(sol.preorderTraversal(root))
print('elapse time: {} sec'.format(time.time() - stime))