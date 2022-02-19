import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import Optional
from typing import List


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

    def get_num_of_groups(self, head: Optional[ListNode], nums: List[int]) -> int:
        def traverse(node):
            values = []
            while node != None:
                values += node.val,
                node = node.next

            return values

        values = traverse(head)
        existences = [False]*len(values)

        for num in nums:
            if num in values:
                existences[values.index(num)] = True

        cnt = 0
        for i in range(len(existences)):
            if not existences[i]:
                if i > 0 and existences[i - 1]:
                    cnt += 1

        if existences[-1]:
            cnt += 1

        return cnt


stime = time.time()
print(Solution().numComponents(create_linked_list_from_nums([3,4,0,2,1]), [1, 3, 4]))
print('elapse time: {} sec'.format(time.time() - stime))