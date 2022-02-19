import time
from util.util_list import *
from util.util_tree import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = head
        t = []
        while None != cur:
            t.append(cur.val)
            cur = cur.next
        if len(t) == 1:
            return head
        n = (len(t)//2)*2
        for i in range(0, n, 2):
            t[i], t[i+1] = t[i+1], t[i]
        cur = ohead = ListNode(t.pop(0))
        while t:
            cur.next = ListNode(t.pop(0))
            cur = cur.next
        return ohead


    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        node = head
        nodes = []
        while node:
            nodes += node,
            node = node.next
        
        n = len(nodes)
        for i in range(0, n-1, 2):
            nodes[i], nodes[i+1] = nodes[i+1], nodes[i]
        
        node = head = nodes.pop(0)
        while nodes:
            node.next = nodes.pop(0)
            node = node.next
        node.next = None
        return head

    def swap_every_two_nodes(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        last = head.next
        head.next = self.swapPairs(head.next.next)
        last.next = head

        return last

    def swap_every_two_nodes(self, node: ListNode) -> ListNode:
        stk = []

        while node:
            stk += node,
            if not node.next:
                break

            node = node.next.next

        next_start = None

        while stk:
            node = stk.pop()
            if not node or not node.next:
                next_start = node
                continue

            last = node.next
            node.next = next_start
            last.next = node
            next_start = last

        return next_start
        

# res = swap_every_two_nodes(create_linked_list_from_nums([2,1,4,3]))
# print(get_nums_from_linked_list(res))

stime = time.time()
print(list_get_nums(Solution().swapPairs(create_linked_list_from_nums([1,2,3]))))
#print(list_get_nums(Solution().swapPairs(create_linked_list_from_nums([2,1,4,3])))) # [[1,5],[6,9]]
print('elapse time: {} sec'.format(time.time() - stime))

