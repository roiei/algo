import time
from util.util_tree import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    histories = []
    def check(self, node, history):
        if node == None:
            self.histories.append(history)
            return
        history.append(node.val)
        self.check(node.left, history[::])
        self.check(node.right, history[::])

    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        self.histories = []
        if root == None:
            return True
        history = []
        self.check(root, history[::])
        print(self.histories)
        n = len(self.histories)
        for i in range(0, n, 2):
            if self.histories[i] != self.histories[n-1-i]:
                return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node, trace, res):
            if not node:
                res += trace[:],
                return

            trace += node.val,
            dfs(node.left, trace, res)
            dfs(node.right, trace, res)
            trace.pop()

        res = []
        dfs(root, [], res)
        n = len(res)
        for i in range(n//2):
            if res[i] != res[n-1-i]:
                return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root]

        while q:
            nq = []
            line = []

            while q:
                node = q.pop(0)
                if not node:
                    line += None,
                else:
                    line += node.val,
                    nq += node.left,
                    nq += node.right,

            if line != line[::-1]:
                return False

            q = nq

        return True



stime = time.time()
print(True == Solution().isSymmetric(deserialize('[1,2,2,3,4,4,3]')))
print(False == Solution().isSymmetric(deserialize('[1,2,2,null,3,null,3]')))
print(False == Solution().isSymmetric(deserialize('[1,2,2,2,null,2]')))
#      1
#    /   \
#   2     2
#  /     /
# 2     2
#
#
#  1
# 2 2
# 2 null 2 null
# null null null null

print('elapse time: {} sec'.format(time.time() - stime))