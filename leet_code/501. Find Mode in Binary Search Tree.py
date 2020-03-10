import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trav(self, root, freq):
        q = []
        q.append(root)
        while q:
            cur = q.pop()
            if cur.val not in freq:
                freq[cur.val] = 1
            else:
                freq[cur.val]+= 1
            if None != cur.left:
                q.append(cur.left)
            if None != cur.right:
                q.append(cur.right)

    def findMode(self, root: TreeNode) -> 'List[int]':
        if not root:
            return []
        freq = {}
        self.trav(root, freq)
        freq = list(sorted(freq.items(), key=lambda param:param[1], reverse=True))
        mfreq = freq[0][1]        
        return [i[0] for i in freq if i[1] == mfreq]


root = TreeNode(1)
root.right = TreeNode(2)

stime = time.time()
sol = Solution()
print(sol.findMode(root)) # 
print('elapse time: {} sec'.format(time.time() - stime)) 