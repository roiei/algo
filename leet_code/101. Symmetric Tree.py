import time

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


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

stime = time.time()
sol = Solution()
print(sol.isSymmetric(root))
print('elapse time: {} sec'.format(time.time() - stime))