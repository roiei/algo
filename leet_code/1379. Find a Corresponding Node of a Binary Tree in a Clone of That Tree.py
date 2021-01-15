class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            
            if node.val == target.val:
                return node
        
            ret = dfs(node.left)
            if ret:
                return ret
            return dfs(node.right)
    
        return dfs(cloned)