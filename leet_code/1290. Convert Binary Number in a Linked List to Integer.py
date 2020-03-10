
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def getDecimalValue(self, head) -> int:
        nums = []
        node = head

        while node:
            nums += node.val,
            node = node.next

        shift = 0
        tot = 0

        for bit in nums[::-1]:
            if bit:
                tot += (1<<shift)

            shift += 1

        return tot


stime = time.time()
print(5 == Solution().getDecimalValue(create_linked_list_from_nums([1,0,1])))
print('elapse time: {} sec'.format(time.time() - stime))