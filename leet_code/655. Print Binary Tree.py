
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []
        def find_depth(node):
            if None == node.left and None == node.right:
                return 1
            ld = rd = 1
            if None != node.left:
                ld = find_depth(node.left) + 1
            if None != node.right:
                rd = find_depth(node.right) + 1
            return max(ld, rd)
        depth = left = find_depth(root)
        length = 1
        while left > 1:
            length = length*2 + 1
            left -= 1
        line = [['' for i in range(length)] for j in range(depth)]
        def dfs(node, line, l, r, depth):
            m = (l+r)//2
            line[depth][m] = str(node.val)
            if None != node.left:
                dfs(node.left, line, l, m-1, depth+1)
            if None != node.right:
                dfs(node.right, line, m+1, r, depth+1)
        dfs(root, line, 0, len(line[0])-1, 0)
        return line
            
