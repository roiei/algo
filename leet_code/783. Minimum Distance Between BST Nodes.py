class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: 'TreeNode') -> int:
        q = []
        q.append(root)
        trace = []
        while q:
            cur = q.pop(0)
            trace.append(cur.val)
            if None != cur.left:
                q.append(cur.left)
            if None != cur.right:
                q.append(cur.right)
        diff = []
        for i in range(len(trace)):
            for j in range(i+1, len(trace)):
                diff.append(abs(trace[i]-trace[j]))
        return min(diff)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

stime = time.time()
sol = Solution()
ret = sol.minDiffInBST(root)
print('elapse time: {} sec'.format(time.time() - stime))
print(ret)