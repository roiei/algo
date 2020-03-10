

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        def level(node):
            q = [node]
            trace = []
            while q:
                t = []
                nq = []
                while q:
                    cur = q.pop(0)
                    t += cur.val,
                    if cur.left != None:
                        nq += cur.left,
                    if cur.right != None:
                        nq += cur.right,
                q = nq
                trace += t,
            return trace
        trace = level(root)
        out = []
        for t in trace:
            out += sum(t)/len(t),
        return out
