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

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = -1
        cnt = 1
        cur = head.val
        node = head.next
        stk = [head]

        while node:
            if node.val == cur:
                cnt += 1
            else:
                if cnt > 1:
                    while cnt:
                        stk.pop()
                        cnt -= 1

                cnt = 1
                cur = node.val

            stk += node,
            node = node.next

        if cnt > 1:
            while cnt:
                stk.pop()
                cnt -= 1

        if not stk:
            return None

        node = head = stk.pop(0)
        while stk:
            node.next = stk.pop(0)
            node = node.next

        node.next = None
        return head
            

stime = time.time()
print(Solution().deleteDuplicates(create_linked_list_from_nums([1,2,3,3,4,4,5])))
print('elapse time: {} sec'.format(time.time() - stime))