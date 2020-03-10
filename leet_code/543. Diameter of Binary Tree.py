class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        mlen = 0
        
        def dfs(node):
            nonlocal mlen
            if not node.left and not node.right:
                return 1
            
            llen = rlen = 0
            if node.left:
                llen = dfs(node.left)
            if node.right:
                rlen = dfs(node.right)
                
            mlen = max(mlen, llen + rlen)
            return max(llen, rlen) + 1
    
        dfs(root)
        return mlen