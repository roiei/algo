
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def get_trace(self, root, trace):
        q = [root]
        while q:
            cur = q.pop(0)
            trace.append(cur.val)
            if None != cur.left:
                q.append(cur.left)
            if None != cur.right:
                q.append(cur.right)        
        
    def getMinimumDifference(self, root: TreeNode) -> int:
        trace = []
        self.get_trace(root, trace)
        if len(trace) < 2:
            return False
        trace.sort()
        print(trace)
        n = len(trace)
        mdiff = 0x7FFFFFFF
        for i in range(n-1):
            diff = abs(trace[i+1]-trace[i])
            #print('{} - {} = {}'.format(trace[i], trace[i-1], diff))
            if mdiff > diff:
                mdiff = diff
        return mdiff

# root = TreeNode(236)
# root.left = TreeNode(104)
# root.right = TreeNode(701)
# root.left.right = TreeNode(227)
# root.right.right = TreeNode(911)

#[543,384,652,null,445,null,699] # 47

root = TreeNode(543)
root.left = TreeNode(384)
root.right = TreeNode(652)
root.left.right = TreeNode(445)
root.right.right = TreeNode(699)

stime = time.time()
print(Solution().getMinimumDifference(root))
print('elapse time: {} sec'.format(time.time() - stime))