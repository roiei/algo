import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = head
        t = []
        while None != cur:
            t.append(cur.val)
            cur = cur.next
        if len(t) == 1:
            return head
        n = (len(t)//2)*2
        for i in range(0, n, 2):
            t[i], t[i+1] = t[i+1], t[i]
        cur = ohead = ListNode(t.pop(0))
        while t:
            cur.next = ListNode(t.pop(0))
            cur = cur.next
        return ohead


    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        node = head
        nodes = []
        while node:
            nodes += node,
            node = node.next
        
        n = len(nodes)
        for i in range(0, n-1, 2):
            nodes[i], nodes[i+1] = nodes[i+1], nodes[i]
        
        node = head = nodes.pop(0)
        while nodes:
            node.next = nodes.pop(0)
            node = node.next
        node.next = None
        

stime = time.time()
print(Solution().swapPairs(None)) # [[1,5],[6,9]]
print('elapse time: {} sec'.format(time.time() - stime))

