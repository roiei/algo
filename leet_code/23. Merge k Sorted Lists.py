from util.util_list import *


class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        trace = []
        for l in lists:
            cur = l
            while None != cur:
                trace.append(cur.val)
                cur = cur.next
        if not trace:
            return None
        trace.sort()
        head = cur = ListNode(trace.pop(0))
        while trace:
            cur.next = ListNode(trace.pop(0))
            cur = cur.next
        return head


