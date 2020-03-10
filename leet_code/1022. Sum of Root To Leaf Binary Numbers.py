

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, seq):
            if not node.left and not node.right:
                seq += str(node.val),
                val = int('0b' + ''.join(seq), 2)
                seq.pop()
                return val

            seq += str(node.val),
            res = []
            if node.left:
                res += dfs(node.left, seq),
            if node.right:
                res += dfs(node.right, seq),
            seq.pop()
            return sum(res)
        
        return dfs(root, [])

