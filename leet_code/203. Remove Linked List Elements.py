class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = head
        pre = head
        while cur != None:
            update = False
            if cur.val == val:
                if cur == head:
                    head = head.next
                else:
                    pre.next = cur.next
                    update = True
            if cur.next == None:
                break
            if False == update:
                pre = cur
            cur = cur.next
        return head


stime = time.time()
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"])) # "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"])) # ""
print('elapse time: {} sec'.format(time.time() - stime)) 