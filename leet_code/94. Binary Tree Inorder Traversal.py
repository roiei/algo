import time
from util_list import *
from util_tree import *


class Solution:
    def traversal_inorder(self, node, t):
        if None != node.left:
            self.traversal_inorder(node.left, t)
        t.append(node.val)
        if None != node.right:
            self.traversal_inorder(node.right, t)

    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        t = []
        self.traversal_inorder(root, t)
        return t


stime = time.time()
print(Solution().inorderTraversal('[1,null,2,3]'))
print('elapse time: {} sec'.format(time.time() - stime))