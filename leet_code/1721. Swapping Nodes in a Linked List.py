
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache
from typing import List
import bisect



class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        
        for _ in range(k - 1):
            fast = fast.next
        first = fast

        # k = 2
        # 1  4  3  2  5
        # s  fa
        #    fi

        # 1  4  3  2  5
        #             fa
        #          s

        while fast.next:
            slow, fast = slow.next, fast.next
        
        first.val, slow.val = slow.val, first.val

        return head

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        def get_prev(node, k):
            prev = None

            while k:
                prev = node
                node = node.next
                k -= 1

            return prev, node

        n = 0
        node = head
        while node:
            node = node.next
            n += 1

        lpre, lnode = get_prev(head, k - 1)
        rpre, rnode = get_prev(head, n - k)

        lnode.val, rnode.val = rnode.val, lnode.val

        return head


stime = time.time()
# 7,9,6,6,7,8,3,0,9,5
#print(list_is_same_list(create_linked_list_from_nums([1,4,3,2,5]), Solution().swapNodes(create_linked_list_from_nums([1,2,3,4,5]), k = 2)))
#print(list_is_same_list(create_linked_list_from_nums([7,9,6,6,8,7,3,0,9,5]), Solution().swapNodes(create_linked_list_from_nums([7,9,6,6,7,8,3,0,9,5]), k = 5)))
#print(list_is_same_list(create_linked_list_from_nums([1]), Solution().swapNodes(create_linked_list_from_nums([1]), k = 1)))
#print(list_is_same_list(create_linked_list_from_nums([2, 1]), Solution().swapNodes(create_linked_list_from_nums([1, 2]), k = 1)))
print(list_is_same_list(create_linked_list_from_nums([90, 100]), Solution().swapNodes(create_linked_list_from_nums([100, 90]), k = 2)))
print('elapse time: {} sec'.format(time.time() - stime))