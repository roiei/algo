
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = [root]
        ts = []
        while q:
            nq = []
            t = []
            while q:
                cur = q.pop()
                t += cur.val,
                if None != cur.left:
                    nq += cur.left,
                if None != cur.right:
                    nq += cur.right,
            q = nq
            ts += t,
        res = []
        for t in ts:
            res += max(t),
        return res

