import heapq

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        def dfs(node, vals):
            heapq.heappush(vals, node.val)
            if None != node.left:
                dfs(node.left, vals)
            if None != node.right:
                dfs(node.right, vals)
            
        vals = []
        dfs(root, vals)
        pm = m = heapq.heappop(vals)
        while vals and m == pm:
            pm = heapq.heappop(vals)       

        return -1 if m == pm else pm

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return []
            
            res = [node.val]
            res += dfs(node.left)
            res += dfs(node.right)
            return res
    
        res = dfs(root)
        res = sorted(list(set(res)))
        
        if not res or len(res) < 2:
            return -1
        
        res.pop(0)
        return res.pop(0)
