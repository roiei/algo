

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        def dfs(node, res):
            res += node.val,
            if node.left:
                dfs(node.left, res)
            if node.right:
                dfs(node.right, res)
        
        seq1 = []
        seq2 = []
        dfs(root1, seq1)
        dfs(root2, seq2)
        
        for val in seq1:
            if target - val in seq2:
                return True
        return False

