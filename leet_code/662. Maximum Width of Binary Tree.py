import time
from util_list import *
from util_tree import *
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




stime = time.time()

#print(Solution().widthOfBinaryTree(deserialize('[1,3,2,5,3,null,9]')))
#print(Solution().widthOfBinaryTree(deserialize('[1,3,2,5]')))
#print(Solution().widthOfBinaryTree(deserialize('[1,1,1,1,null,null,1,1,null,null,1]')))
print(Solution().widthOfBinaryTree(deserialize('[1,null,2]')))
#print(Solution().openLock(["0201","0101","0102","1212","2002"], '0202'))
print('elapse time: {} sec'.format(time.time() - stime))