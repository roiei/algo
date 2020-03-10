import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None
        trace = []
        cur = head
        while None != cur:
            if cur in trace:
                return cur
            trace.append(cur)
            cur = cur.next


stime = time.time()
print(Solution().detectCycle(create_linked_list('3->2->0->-4')))
print('elapse time: {} sec'.format(time.time() - stime))