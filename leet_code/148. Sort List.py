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
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        # 런너 기법 활용
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        # 분할 재귀 호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)


stime = time.time()
print([1, 2, 3, 4] == list_get_nums(Solution().sortList(create_linked_list('4->2->1->3'))))
print('elapse time: {} sec'.format(time.time() - stime))