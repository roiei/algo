from util.util_list import *


class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        cur = head;
        if None == cur:
            return 
        t = []
        while None != cur:
            t.append(cur.val)
            cur = cur.next
        rhead = ListNode(t[-1]); t.pop()
        cur = rhead
        while t:
            cur.next = ListNode(t.pop())
            cur = cur.next
        return rhead

