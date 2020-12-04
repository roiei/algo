import time
from util.util_list import *


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

    def isPalindrome(self, head: ListNode) -> bool:


stime = time.time()
print(False == Solution().reverseList(create_linked_list('1->2')))
print(True == Solution().reverseList(create_linked_list('1->2->2->1')))
print('elapse time: {} sec'.format(time.time() - stime))