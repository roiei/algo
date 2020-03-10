
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        nodes = []
        while head:
            nodes += head,
            head = head.next
        return nodes[len(nodes)//2]