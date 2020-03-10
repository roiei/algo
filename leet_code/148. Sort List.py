import time
import sys
from util.util_list import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def traverse(node):
            res = []
            while node:
                res += node.val,
                node = node.next
            return res
        
        vals = traverse(head)
        
        def search(nums, target):
            l = 0
            r = len(nums)-1
            while l <= r:
                m = (l + r)//2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        snums = []
        for val in vals:
            idx = search(snums, val)
            snums.insert(idx, val)
        
        def create(nums):
            if not nums:
                return None
            node = head = ListNode(nums[0])
            for i in range(1, len(nums)):
                node.next = ListNode(nums[i])
                node = node.next
            return head
    
        return create(snums)
        


def create_linked_list(numstr):
    nums = list(map(int, numstr.split('->')))
    if not nums:
        return None
    head = cur = ListNode(nums.pop(0))
    while nums:
        cur.next = ListNode(nums.pop(0))
        cur = cur.next
    return head


stime = time.time()

print(Solution().sortList(create_linked_list('4->2->1->3')))
print('elapse time: {} sec'.format(time.time() - stime))