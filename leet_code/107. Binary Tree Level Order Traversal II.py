class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traverse_level_order(self, root, trace):
        q = []
        q.append([root, 1])
        while q:
            cur = q.pop(0)
            trace.append([cur[0].val, cur[1]])
            if None != cur[0].left:
                q.append([cur[0].left, cur[1]+1])
            if None != cur[0].right:
                q.append([cur[0].right, cur[1]+1])

    def levelOrderBottom(self, root: TreeNode) -> 'List[List[int]]':
        if not root:
            return []
        trace = []
        self.traverse_level_order(root, trace)
        trace.sort(key=lambda param:param[1], reverse=True)
        levels = []
        level = []
        pre = trace[0][1]
        while trace:
            t = trace.pop(0)
            if pre != t[1]:
                levels.append(level)
                level = []
                pre = t[1]
            level.append(t[0])
            if not trace:
                levels.append(level)
        return levels

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

stime = time.time()
sol = Solution()
print(sol.levelOrderBottom(root))
print('elapse time: {} sec'.format(time.time() - stime))