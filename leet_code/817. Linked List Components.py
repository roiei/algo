import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def numComponents(self, head: ListNode, G: [int]) -> int:
        def traverse(node):
            t = []
            while node != None:
                t += node.val,
                node = node.next
            return t
        t = traverse(head)
        con = [False]*len(t)
        for g in G:
            if g in t:
                con[t.index(g)] = True
        cnt = 0
        num = 0
        for i in range(len(con)):
            if True == con[i]:
                num += 1
                if i == len(con)-1:
                    cnt += 1
            elif False == con[i] and num > 0:
                cnt += 1
                num = 0
        return cnt


stime = time.time()
print(1 == Solution().numComponents(create_list('3,4,0,2,1', ','), [4]))
print('elapse time: {} sec'.format(time.time() - stime))