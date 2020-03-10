
import math
import heapq
import time


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def tra(self, node, trace):
        while None != node:
            trace.append(node)
            node = node.next
            
    def getIntersectionNode(self, headA, headB):
        trace_a = []
        trace_b = []
        self.tra(headA, trace_a)
        self.tra(headB, trace_b)
        res = None
        while trace_a and trace_b:
            if trace_a[-1] == trace_b[-1]:
                res = trace_a[-1]
            else:
                break
            trace_a.pop()
            trace_b.pop()
        return res


stime = time.time()
sol = Solution()
print(sol.findMaximumXOR([3, 10, 5, 25, 2, 8]))
print(sol.findMaximumXOR(nums))
print('elapse time: {} sec'.format(time.time() - stime))
