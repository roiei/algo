
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        seq = []
        while head:
            seq += head.val,
            head = head.next

        while True:
            tot = 0
            idxs = collections.defaultdict(int)
            idxs[0] = -1
            start = end = None

            for i, num in enumerate(seq):
                tot += num
                if tot in idxs:
                    start = idxs[tot]
                    end = i
                    break
                idxs[tot] = i
                
            if start == end == None:
                break
            
            length = end - start
            seq = seq[:start + 1] + seq[end + 1:]
        
        return seq


stime = time.time()
print([3,1] == Solution().removeZeroSumSublists(create_linked_list_from_nums([1,2,-3,3,1])))
print([1,2,4] == Solution().removeZeroSumSublists(create_linked_list_from_nums([1,2,3,-3,4])))
print('elapse time: {} sec'.format(time.time() - stime))