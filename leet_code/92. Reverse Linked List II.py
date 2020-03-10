
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        rcur = cur = head
        stk = []
        i = 1
        while None != cur:
            if i < m:
                rcur = cur
            elif m <= i <= n:
                stk += cur,
            if i == n+1 or None == cur.next:
                if stk:
                    n = len(stk)
                    for j in range(n//2):
                        stk[j].val, stk[n-1-j].val = stk[n-1-j].val, stk[j].val
                stk = []
            cur = cur.next
            i += 1
        return head

