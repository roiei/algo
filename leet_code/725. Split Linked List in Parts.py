
import time
from util.util_list import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> 'List[ListNode]':
        n = 0
        cur = root
        while cur != None:
            cur = cur.next
            n += 1
        unit = n//k
        sunit = 0
        remain = 0
        if 0 == unit:
            unit = 1
        else:
            remain = n - unit*k
        sunit = unit
        if 0 < remain:
            sunit += 1
            remain -= 1
        cur = root
        part = []
        parts = []
        while cur != None:
            if 0 == sunit:
                sunit = unit
                if 0 < remain:
                    sunit += 1
                    remain -= 1
                parts.append(part)
                part = []
            part.append(cur.val)
            sunit-= 1
            cur = cur.next
            if None == cur:
                parts.append(part)
        if len(parts) < k:
            pad_len = k - len(parts)
            for i in range(pad_len):
                parts.append([])
        return parts

    def splitListToParts(self, root, k):
        if not root:
            return [None for _ in range(k)]

        seq = []
        while root:
            seq += root,
            root = root.next
        
        n = len(seq)
        
        pad = 0
        if n < k:
            pad = k - n
            k = n
        
        part = n//k
        left = n%k
        
        sizes = []
        
        for i in range(k):
            add = 0
            if left > 0:
                add = 1
                left -= 1
            sizes += part + add,
        
        print('sizes = ', sizes)
        
        res = []
        i = 0
        while i < n:
            res += seq[i],
            if i > 0:
                seq[i - 1].next = None
            
            i += sizes.pop(0)           
                
        while pad:
            res += None,
            pad -= 1
        
        return res


stime = time.time()
#print(Solution().splitListToParts(create_linked_list_from_nums([1, 2, 3]), 3))
print(Solution().splitListToParts(create_linked_list_from_nums([]), 3))
print('elapse time: {} sec'.format(time.time() - stime))
