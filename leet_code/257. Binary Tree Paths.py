
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TraceInfo:
    def __init__(self, val, parent, is_leaf):
        self.val = val
        self.parent = parent
        self.is_leaf = is_leaf

class Solution:
    def is_leaf(self, node):
        return True if node.left == None and node.right == None else False

    def level_order(self, root, trace):
        root_info = TraceInfo(root.val, None, self.is_leaf(root))
        trace.append(root_info)
        q = []
        q.append([root, root_info])
        while q:
            cur, pinfo = q.pop(0)
            if None != cur.left:
                info = TraceInfo(cur.left.val, pinfo, self.is_leaf(cur.left))
                q.append([cur.left, info])
                trace.append(info)
            if None != cur.right:
                info = TraceInfo(cur.right.val, pinfo, self.is_leaf(cur.right))
                q.append([cur.right, info])
                trace.append(info)

    def binaryTreePaths2(self, root: TreeNode) -> 'List[str]':
        trace = []
        self.level_order(root, trace)
        leafs = [t for t in trace if True == t.is_leaf]
        paths = []
        for leaf in leafs:
            cur = leaf
            path = []
            while None != cur.parent:
                path.append(cur.val)
                cur = cur.parent
            path.append(root.val)
            paths.append(path[::-1])
        spaths = []
        for path in paths:
            spath = ''
            for i in range(len(path)):
                spath += str(path[i])
                if i < len(path)-1:
                    spath += str('->')
            spaths.append(spath)
        return spaths

    def tra(self, node, trace, res):
        trace.append(node.val)
        if None == node.left and None == node.right:
            res.append(trace[:])
            trace.pop()
            return
        if None != node.left:
            self.tra(node.left, trace, res)
        if None != node.right:
            self.tra(node.right, trace, res)
        trace.pop()

    def binaryTreePaths(self, root):
        res = []
        self.tra(root, [], res)
        out = []
        for r in res:
            out.append('->'.join([str(v) for v in r]))
        return out



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)

# ["1->2->5", "1->3"]

stime = time.time()
sol = Solution()
print(sol.binaryTreePaths2(root))
print(sol.binaryTreePaths(root))
print('elapse time: {} sec'.format(time.time() - stime))
