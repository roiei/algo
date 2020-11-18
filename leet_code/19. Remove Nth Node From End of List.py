import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        def trav(head):
            cur = head
            cnt = 0
            while None != cur:
                cnt += 1
                cur = cur.next
            return cnt
        cnt = trav(head)
        def remove(head, cnt, n):
            pre = cur = head
            left = cnt - n
            while None != cur:
                if 0 == left:
                    if cur == head:
                        return True
                    else:
                        pre.next = cur.next
                    break
                pre = cur
                cur = cur.next
                left -= 1
            return False
        if True == remove(head, cnt, n):
            head = head.next
        return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        cur = head

        while cur:
            nodes += cur,
            cur = cur.next

        if len(nodes) == 1 and n == 1:
            return None

        if len(nodes) == n:
            return nodes[-(n - 1)]

        if n == 1:
            nodes[-(n + 1)].next = None
        elif len(nodes) > n:
            nodes[-(n + 1)].next = nodes[-(n - 1)]

        return head


stime = time.time()
#print(Solution().removeNthFromEnd(create_linked_list('1->2->3->4->5'), 2))
#print(list_traverse(Solution().removeNthFromEnd(create_linked_list('1'), 1)))
print(list_traverse(Solution().removeNthFromEnd(create_linked_list('1->2'), 1)))
print('elapse time: {} sec'.format(time.time() - stime))