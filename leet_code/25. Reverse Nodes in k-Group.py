import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or 1 >= k:
            return head
        cur = pos = head
        while None != cur:
            i, left = 0, k
            nodes = [None]*k
            while None != pos and left > 0:
                nodes[i] = pos
                pos = pos.next
                i += 1
                left -= 1
            if i == k:
                nodes.reverse()
            if head == cur:
                cur = head = nodes[0]
                for j in range(1, k):
                    if None == nodes[j]:
                        break
                    cur.next = nodes[j]
                    cur = cur.next
                cur.next = None
            else:                
                for j in range(k):
                    if None == nodes[j]:
                        continue
                    cur.next = nodes[j]
                    cur = cur.next
                cur.next = None
            if i < k:
                break
        return head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        nodes = []
        while head:
            nodes += head,
            head = head.next

        for i in range(0, len(nodes) - k + 1, k):
            nodes[i:i + k] = nodes[i:i + k][::-1]

        cur = rhead = nodes[0]
        for i in range(1, len(nodes)):
            cur.next = nodes[i]
            cur = cur.next
        cur.next = None

        return rhead



stime = time.time()
#print(Solution().reverseKGroup(create_linked_list('1->2->3->4->5'), 4))
print(Solution().reverseKGroup(create_linked_list('1->2->3->4->5'), 2))
print('elapse time: {} sec'.format(time.time() - stime))