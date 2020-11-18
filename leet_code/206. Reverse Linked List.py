from util.util_list import *


class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if None == head:
            return None

        cur = head;
        t = []

        while cur:
            t += cur,
            cur = cur.next

        for i in range(len(t) - 1, 0, -1):
            t[i].next = t[i - 1]

        t[0].next = None
        return t[-1]

    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return None

        def dfs(node, head):
            if not node.next:
                head += node,
                return node

            pre = None
            if node.next:
                pre = dfs(node.next, head)
                pre.next = node

            return node

        res = []
        node = dfs(head, res)
        node.next = None
        return res[0]


print(list_traverse(Solution().reverseList(create_linked_list('1->2->3->4->5'))))
