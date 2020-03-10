
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        def dfs(node):
            if node.left == None and node.right == None:
                return [node.val]
            res = [node.val]
            if node.left != None:
                res += dfs(node.left)
            if node.right != None:
                res += dfs(node.right)
            return res
        vals = dfs(root)
        vals = [val for val in vals if val != None]
        return True if vals.count(vals[0]) == len(vals) else False