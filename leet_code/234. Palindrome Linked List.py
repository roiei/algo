
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def trace(node):
            t = []
            cur = node
            while cur != None:
                t += cur.val,
                cur = cur.next
            return t
        t = trace(head)
        if t == t[::-1]:
            return True
        return False

