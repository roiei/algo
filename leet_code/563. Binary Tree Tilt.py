import time

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def get_tile(self, node):
        if None == node.left and None == node.right:
            return 0
        lt = rt = 0
        lv = rv = 0
        if None != node.left:
            lt = self.get_tile(node.left)
            lv = node.left.val
        if None != node.right:
            rt = self.get_tile(node.right)
            rv = node.right.val

        return abs(lv-rv) + lt + rt

    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.get_tile(root)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)

# [1,2,3,4,null,5] -> 11
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)

stime = time.time()
print(Solution().findTilt(root))
print('elapse time: {} sec'.format(time.time() - stime))