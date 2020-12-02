from util.util_list import *


class Solution:
    def traverse(self, node):
        t = []
        while None != node:
            t.append(node.val)
            node = node.next
        return t
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        t  = self.traverse(l1)
        t += self.traverse(l2)
        t.sort()
        if not t:
            return
        head = cur = ListNode(t.pop(0))
        while t:
            cur.next = ListNode(t.pop(0))
            cur = cur.next
        return head

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2

        cur = res_head = ListNode(None)

        while cur1 or cur2:
            if cur1 and cur2:
                if cur1.val < cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
            elif cur1 and not cur2:
                cur.next = cur1
                cur1 = cur1.next
            elif not cur1 and cur2:
                cur.next = cur2
                cur2 = cur2.next

            cur = cur.next

        return res_head.next


print(list_traverse(Solution().mergeTwoLists(create_linked_list('1->2->4'), create_linked_list('1->3->4'))))
print(list_traverse(Solution().mergeTwoLists(None, create_linked_list('0'))))



