
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return False
        
        def dfs(node, leafs):
            if None == node.left and None == node.right:
                leafs += node.val,
            if None != node.left:
                dfs(node.left, leafs)
            if None != node.right:
                dfs(node.right, leafs)
            
        leafs1 = []
        dfs(root1, leafs1)
        leafs2 = []
        dfs(root2, leafs2)
        return True if leafs1 == leafs2 else False

