import time
from util.util_list import *


class Solution:
    def tra(self, node):
        while None != node:
            print(node.val, end=' -> ')
            node = node.next
        print()

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        target = head
        target_pre = target

        while None != target:
            cur_pre = cur = head
            found = False

            while cur != target:
                if cur.val > target.val:
                    found = True
                    break
                cur_pre = cur
                cur = cur.next

            if True == found:
                if cur_pre != cur:
                    cur_pre.next = target
                else:
                    head = target
                    
                target_pre.next = target.next
                target.next = cur
                target = target_pre

            target_pre = target
            target = target.next

        return head



stime = time.time()

#print(Solution().insertionSortList(create_linked_list('4->2->1->3')))
print(Solution().insertionSortList(create_linked_list('-1->5->3->4->0')))
print('elapse time: {} sec'.format(time.time() - stime))