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

    def rotate_list(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        n = 0
        node = head
        last = None

        while node:
            if node:
                last = node
            node = node.next
            n += 1

        k = k % n

        if n == 1 or k == 0 or k == n:
            return head
        
        i = 0
        pre = node = head

        while node and i < n - k:
            pre = node
            node = node.next
            i += 1

        last.next = head
        pre.next = None
        head = node

        return head

head = rotate_list(create_linked_list_from_nums([6, 7, 4, 3]), 2)
print(list_get_nums(head))

stime = time.time()
print([4, 3, 6, 7] == list_get_nums(Solution().rotateRight(create_linked_list_from_nums([6, 7, 4, 3]), 2)))
#print(list_get_nums(Solution().rotateRight(create_linked_list_from_nums([1]), 0)))
print('elapse time: {} sec'.format(time.time() - stime))