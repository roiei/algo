import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_nums(node):
            res = []
            while node:
                res += node.val,
                node = node.next
            return res
    
        val1 = int(''.join(str(val) for val in get_nums(l1)))
        val2 = int(''.join(str(val) for val in get_nums(l2)))
        vals = [int(val) for val in str(val1 + val2)]
        if not vals:
            return None
        node = res = ListNode(vals.pop(0))
        while vals:
            node.next = ListNode(vals.pop(0))
            node = node.next

        print(list_get_nums(res))
        return res
                       


stime = time.time()
print([7, 8, 0, 7] == list_get_nums(Solution().addTwoNumbers(create_linked_list_from_nums([7, 2, 4, 3]), create_linked_list_from_nums([5, 6, 4]))))
print('elapse time: {} sec'.format(time.time() - stime))
