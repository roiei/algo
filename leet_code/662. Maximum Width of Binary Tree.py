import time
from util.util_list import *
from util.util_tree import *
import copy
import collections



class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [[root, 1]]
        ts = []
        while q:
            nq = []
            t = []
            while q:
                cur, idx = q.pop(0)
                if None == cur:
                    t += [None, idx],
                    continue
                else:
                    t += [cur.val, idx],
                
                nq += [cur.left, idx*2-1],
                nq += [cur.right, idx*2],
            q = nq
            ts += t,
        
        for t in ts:
            while t and None == t[-1][0]:
                t.pop()
            while t and None == t[0][0]:
                t.pop(0)

        lens = []
        for t in ts:
            if not t:
                continue
            lens += t[-1][1]-t[0][1]+1,
        return max(lens)

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = [(root, 0)]
        seqs = []

        while q:
            seq = []
            nq = []

            while q:
                node, idx = q.pop(0)
                if not node:
                    seq += (None, idx),
                    continue

                seq += (node.val, idx),
                nq += (node.left, idx*2),
                nq += (node.right, idx*2 + 1),

            q = nq
            seqs += seq,

        mx = 0
        for seq in seqs:
            while seq and None == seq[0][0]:
                seq.pop(0)

            while seq and None == seq[-1][0]:
                seq.pop()

            if not seq:
                continue

            mx = max(mx, seq[-1][1] - seq[0][1] + 1)

        return mx

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        depths = collections.defaultdict(list)
        
        def dfs(node, depth, pos):
            if not node:
                return
        
            depths[depth] += pos,
            
            dfs(node.left, depth + 1, pos*2 - 1)
            dfs(node.right, depth + 1, pos*2)
        
        dfs(root, 0, 1)

        mx = 0
        for value in depths.values():
            mx = max(mx, max(value) - min(value) + 1)

        return mx

    def get_max_level_width(self, root: TreeNode) -> int:
        q = collections.deque([(root, 1)])
        mx_width = 0

        while q:
            nq = collections.deque()
            idx = first = q[0][1]

            while q:
                node, idx = q.popleft()

                if node.left:
                    nq += (node.left, idx * 2 - 1),
                if node.right:
                    nq += (node.right, idx * 2),

            mx_width = max(mx_width, idx - first + 1)
            q = nq

        return mx_width



get_max_level_width

stime = time.time()
# print(4 == Solution().widthOfBinaryTree(deserialize('[1,3,2,5,3,null,9]')))
print(4 == Solution().widthOfBinaryTree(deserialize('[1, 2, 3, null, 4, null, 6, null, 7, 10]')))
#print(2 == Solution().widthOfBinaryTree(deserialize('[1,3,2,5]')))
# print(1 == Solution().widthOfBinaryTree(deserialize('[0]')))
# print(8 == Solution().widthOfBinaryTree(deserialize('[1,1,1,1,null,null,1,1,null,null,1]')))
# print(1 == Solution().widthOfBinaryTree(deserialize('[1,null,2]')))
print('elapse time: {} sec'.format(time.time() - stime))