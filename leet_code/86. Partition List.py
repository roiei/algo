import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        bef = []
        aft = []
        node = head
        while node != None:
            if node.val < x:
                bef += node.val,
            else:
                aft += node.val,
            node = node.next
        rhead = None
        if bef:
            rhead = ListNode(bef.pop(0))
        else:
            rhead = ListNode(aft.pop(0))
        
        node = rhead
        while bef:
            node.next = ListNode(bef.pop(0))
            node = node.next
        while aft:
            node.next = ListNode(aft.pop(0))
            node = node.next
        return rhead
            

stime = time.time()
print(Solution().partition(create_list('1->4->3->2->5->2', '->'), 3))
print('elapse time: {} sec'.format(time.time() - stime))