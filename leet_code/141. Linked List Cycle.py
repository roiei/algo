# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cycle = False
        trace = []
        cur = head
        while None != cur:
            if cur in trace:
                cycle = True
                break
            trace.append(cur)
            cur = cur.next

        return cycle
        
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next


sol = Solution()
ret = sol.hasCycle(head)
print(ret)