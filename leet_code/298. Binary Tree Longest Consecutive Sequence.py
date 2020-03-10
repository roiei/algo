import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def longestConsecutiveSequence(self, root):
        if not root:
            return 0

        def dfs(node, record):
            if None == node.left and None == node.right:
                record += [node.val, 1],
                return node.val, 1

            cur_cnt = 1
            if None != node.left:
                prev, ccnt = dfs(node.left, record)
                if prev == node.val+1:
                    ccnt += 1
                    cur_cnt = max(cur_cnt, ccnt)
            if None != node.right:
                prev, ccnt = dfs(node.right, record)
                if prev == node.val+1:
                    ccnt += 1
                    cur_cnt = max(cur_cnt, ccnt)

            record += [node.val, cur_cnt],
            return node.val, cur_cnt

        record = []
        dfs(root, record)
        record.sort(key=lambda p:p[1], reverse=True)
        return record[0][0]


    def longestConsecutive(self, root):
        if not root:
            return 0

        mlen = 0

        def dfs(node):
            nonlocal mlen
            if not node:
                return 0
            
            if not node.left and not node.right:
                return 1
                
            l_len = dfs(node.left)
            r_len = dfs(node.right)

            l_len = l_len + 1 if node.left and node.val + 1 == node.left.val else 1
            r_len = r_len + 1 if node.right and node.val + 1 == node.right.val else 1

            clen = max(l_len, r_len)
            mlen = max(mlen, clen)
            return clen
        
        dfs(root)
        return mlen


stime = time.time()
print(3 == Solution().longestConsecutive(deserialize('[1,null,2,null,4,null,5,null,6]')))
print(Solution().longestConsecutive(deserialize('[3,2,1]')))
#print(Solution().longestConsecutiveSequence(deserialize('[1,null,3,2,4,null,null,null,5]')))
#print(Solution().longestConsecutiveSequence(deserialize('[2,null,3,2,null,1,null]')))
print('elapse time: {} sec'.format(time.time() - stime))