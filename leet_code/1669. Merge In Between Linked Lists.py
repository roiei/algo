import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        nodes = []
        cur = list1
        while cur:
            nodes += cur,
            cur = cur.next
        
        pad_nodes = []
        cur = list2
        while cur:
            pad_nodes += cur,
            cur = cur.next
        
        nodes[a:b + 1] = pad_nodes
        
        head = cur = nodes.pop(0)
        while nodes:
            cur.next = nodes.pop(0)
            cur = cur.next
        
        return head

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pre = cur = list1
        i = 0
        
        while cur:
            if a <= i <= b:
                while list2:
                    pre.next = list2
                    pre = pre.next
                    list2 = list2.next
                
                while i <= b:
                    cur = cur.next
                    i += 1
                
                pre.next = cur
            
            pre = cur
            cur = cur.next
            i += 1
        
        return list1


stime = time.time()
print([0,1,2,1000000,1000001,1000002,5] == 
	list_get_nums(
		Solution().mergeInBetween(create_linked_list_from_nums([0,1,2,3,4,5]), 3, 4, create_linked_list_from_nums([1000000,1000001,1000002]))
	))
print('elapse time: {} sec'.format(time.time() - stime))
