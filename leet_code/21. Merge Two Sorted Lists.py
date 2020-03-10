from util.util_list import *


class Solution:
    def traverse(self, node):
        t = []
        while None != node:
            t.append(node.val)
            node = node.next
        return t
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        t  = self.traverse(l1)
        t += self.traverse(l2)
        t.sort()
        if not t:
            return
        head = cur = ListNode(t.pop(0))
        while t:
            cur.next = ListNode(t.pop(0))
            cur = cur.next
        return head

