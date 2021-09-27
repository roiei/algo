
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

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(node1, node2):            
            if not node1 and not node2:
                return True
        
            if not node1 or not node2:
                return False
        
            if node1.val != node2.val:
                return False
        
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
    
        return dfs(p, q)

