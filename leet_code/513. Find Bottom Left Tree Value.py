
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return -1
    
        trace = []
        q = [root]
        while q:
            nq = []
            t = []
            while q:
                cur = q.pop(0)
                t += cur.val,
                if None != cur.left:
                    nq += cur.left,
                if None != cur.right:
                    nq += cur.right,
            trace += t,
            q = nq
        
        return trace[-1][0]

