import time
from util_list import *
from util_tree import *


class Solution:
    def traverse_post(self, node, trace):
        if None != node.left:
            self.traverse_post(node.left, trace)
        if None != node.right:
            self.traverse_post(node.right, trace)
        trace.append(node.val)

    def postorderTraversal(self, root: TreeNode) -> 'List[int]':
        res = []
        if not root:
            return res
        self.traverse_post(root, res)
        return res


stime = time.time()
print(Solution().postorderTraversal(deserialize('[1,null,2,3]')))
print('elapse time: {} sec'.format(time.time() - stime))