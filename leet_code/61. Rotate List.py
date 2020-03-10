import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        def traverse(head):
            res = []
            cur = head
            while cur != None:
                res += cur,
                cur = cur.next
            return res
        stk = traverse(head)
        n = len(stk)
        k = k%n
        while k:
            node = stk.pop()
            node.next = head
            head = node
            stk[-1].next = None
            k -= 1
        return head


stime = time.time()
print(Solution().minCostClimbingStairs([0, 0, 0, 1]))
#print(15 == Solution().minCostClimbingStairs([10, 15, 20]))
#print(6 == Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print('elapse time: {} sec'.format(time.time() - stime))