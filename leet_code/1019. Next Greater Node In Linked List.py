import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
from typing import List 


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.insert(0, head.val)
            head = head.next

        stk = []
        res = []

        for num in nums:
            while stk and stk[-1] <= num:
                stk.pop()

            if not stk:
                res.insert(0, 0)
            else:
                res.insert(0, stk[-1])
            
            stk += num,

        return res


stime = time.time()
print([7,9,9,9,0,5,0,0] == Solution().nextLargerNodes(create_linked_list_from_nums([1,7,5,1,9,2,5,1])))
print([0,0] == Solution().nextLargerNodes(create_linked_list_from_nums([3,3])))
print('elapse time: {} sec'.format(time.time() - stime))