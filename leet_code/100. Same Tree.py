
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return []
            q = [node]
            ts = []
            while q:
                nq = []
                t = []
                while q:
                    cur = q.pop(0)
                    if None == cur:
                        t += None,
                        continue
                    t += cur.val,
                    nq += cur.left,
                    nq += cur.right,
                q = nq
                ts += t,
            return ts
        return True if dfs(p) == dfs(q) else False

