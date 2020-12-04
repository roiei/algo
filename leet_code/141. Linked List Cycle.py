from util.util_list import *


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

    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        
        return False


head = create_linked_list_from_nums([3,2,0,-4])
head.next.next.next.next = head.next
print(True == Solution().hasCycle(head))
