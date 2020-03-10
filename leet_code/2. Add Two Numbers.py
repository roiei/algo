
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers_old(self, l1: ListNode, l2: ListNode) -> ListNode:
        val1 = val2 = ''
        while None != l1:
            val1 += str(l1.val)
            l1 = l1.next
        while None != l2:
            val2 += str(l2.val)
            l2 = l2.next
        ival1 = int(val1[::-1])
        ival2 = int(val2[::-1])
        sval = str(ival1 + ival2)
        node = None
        pre_node = None
        for i in sval:
            node = ListNode(int(i))
            node.next = pre_node
            pre_node = node
        return node

    def tra(self, node):
        t = []        
        while None != node:            
            t.append(node.val)
            node = node.next
        return t
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1 = self.tra(l1)
        t2 = self.tra(l2)
        t1.reverse()
        t2.reverse()
        val = int(''.join([str(v) for v in t1])) + int(''.join([str(v) for v in t2]))
        val = list(str(val))
        val.reverse()
        if not val:
            return None
        rnode = cur = ListNode(int(val.pop(0)))
        while val:            
            cur.next = ListNode(int(val.pop(0)))
            cur = cur.next
        return rnode


l1 = ListNode(5)
l2 = ListNode(5)


stime = time.time()
sol = Solution()
print(sol.addTwoNumbers(l1, l2))
print('elapse time: {} sec'.format(time.time() - stime))