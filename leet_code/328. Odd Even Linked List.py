
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        even = []
        odd = []
        cnt = 1
        while head:
            if cnt%2 == 0:
                even += head,
            else:
                odd += head,
            head = head.next
            cnt += 1
        out = odd.pop(0)
        cur = out
        while odd:
            cur.next = odd.pop(0)
            cur = cur.next
        while even:
            cur.next = even.pop(0)
            cur = cur.next
        cur.next = None
        return out
