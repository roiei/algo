import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        freq = collections.defaultdict(int)
        t = []
        node = head
        while node != None:
            freq[node.val] += 1
            t += node.val,
            node = node.next
        rhead = None
        while t:
            cur = t.pop(0)
            if freq[cur] == 1:
                rhead = ListNode(cur)
                break
        node = rhead
        while t:
            cur = t.pop(0)
            if freq[cur] == 1:
                node.next = ListNode(cur)
                node = node.next
        return rhead
            

stime = time.time()
print(Solution().deleteDuplicates(create_list('1->2->3->3->4->4->5', '->')))
print('elapse time: {} sec'.format(time.time() - stime))