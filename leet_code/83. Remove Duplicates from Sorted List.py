import time
from util.util_list import *


class Solution:
    def traverse(self, node):
        t = []
        while None != node:
            t.append(node.val)
            node = node.next
        return t
        
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t = self.traverse(head)
        if not t:
            return None
        ts = set()
        t = [v for v in t if v not in ts and not ts.add(v)]
        if not t:
            return None
        head = cur = ListNode(t.pop(0))
        while t:
            cur.next = ListNode(t.pop(0))
            cur = cur.next
        return head
        





stime = time.time()

print(Solution().deleteDuplicates(create_linked_list('1->1->2')))
print('elapse time: {} sec'.format(time.time() - stime))