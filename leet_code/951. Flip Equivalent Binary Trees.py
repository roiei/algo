
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            ret1 = dfs(node1.left, node2.left) and \
                dfs(node1.right, node2.right)

            ret2 = ret1 or (dfs(node1.left, node2.right) and 
                dfs(node1.right, node2.left))
            return ret2

        return dfs(root1, root2)

