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
