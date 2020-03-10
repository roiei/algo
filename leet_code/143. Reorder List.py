import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        nodes = []
        cur = head
        n = 0
        while cur != None:
            nodes += cur,
            cur = cur.next
            n += 1

        if 0 != n%2:
            nodes.insert(n//2+1, None)
            n += 1
        
        cur = head
        for i in range(n//2):
            if 0 != i:
                cur.next = nodes[i]
                cur = cur.next
            if None != nodes[n-1-i]:
                cur.next = nodes[n-1-i]
                cur = cur.next
        cur.next = None
            

            

stime = time.time()
print(Solution().reorderList(create_linked_list_from_nums([1,2,3,4,5])))
print('elapse time: {} sec'.format(time.time() - stime))