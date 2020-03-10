

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        q = [root]
        trace = []
        while q:
            nq = []
            t = []
            while q:
                cur = q.pop(0)
                if None == cur:
                    t += 'null',
                    continue
                t += cur.val,
                nq += cur.left,
                nq += cur.right,
            q = nq
            trace += [t]
        reverse = []
        for t in trace:
            for val in reversed(t):
                reverse += [val]
        
        while None == reverse[-1]:
            reverse.pop()
        print(reverse)

        rh = TreeNode(reverse.pop(0))
        q = [rh]
        while reverse:
            cur = q.pop(0)
            cur.left = TreeNode(reverse.pop(0))
            if cur.left:
                q += [cur.left]
            if reverse:
                cur.right = TreeNode(reverse.pop(0))
                if cur.right:
                    q += [cur.right]
        return rh

print(Solution().invertTree(deserialize('[1, 2]')))
#print(Solution().invertTree(deserialize('[4,2,7,1,3,6,9]')))
