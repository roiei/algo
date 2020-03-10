
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def insert(self, node, x):
        def search(nodes, target):
            l = 0
            r = len(nodes) - 1

            while l <= r:
                m = (l + r)//2
                if nodes[m].val == target:
                    return m
                if nodes[m].val < target:
                    l = m + 1
                else:
                    r = m - 1
            return l

        def search_pivot(nodes, l, r, target):
            if l > r:
                return -1

            m = (l + r)//2
            if m + 1 <= r and nodes[m].val > nodes[m + 1].val:
                return m + 1

            lidx = search_pivot(nodes, l, m - 1, target)
            ridx = search_pivot(nodes, m + 1, r, target)
            if lidx != -1:
                return lidx
            return ridx

        nodes = []
        ptr = node
        while ptr:
            if ptr in nodes:
                break
            nodes += ptr,
            ptr = ptr.next

        mi = 0
        if len(nodes) > 1:
            mi = search_pivot(nodes, 0, len(nodes) - 1, x)
        elif len(nodes) == 1 and nodes[0].val < x:
            mi = 1

        nodes = nodes[mi:] + nodes[:mi]
        idx = search(nodes, x)
        x = ListNode(x)

        if nodes and idx == len(nodes):
            nodes[-1].next = x
            x.next = nodes[0]
            return node
        elif nodes and idx == 0:
            x.next = nodes[0]
            nodes[-1].next = x
            return x
        elif not nodes:
            x.next = x
            return x

        nodes[idx - 1].next = x
        x.next = nodes[idx]
        return nodes[0]


    def insert(self, node, x):
        originNode = node
        tmp = ListNode(x)
        if node == None:
            node = tmp
            node.next = node
            return node

        while True:
            if node.next.next == node:
                tmp.next = node.next
                node.next = tmp
                return node

            if (node.val<=x and node.next.val>x) or (node.val<x and node.next.val>=x) or (node.val>node.next.val and node.val<x and node.next.val<x) or (node.val>node.next.val and node.val>x and node.next.val>x):
                tmp.next = node.next
                node.next = tmp
                return node

            node = node.next
            if node == originNode:
                tmp.next = node.next
                node.next = tmp
                return node


def print_cycle_list(alist, info=''):
    print('+print : ', info)
    cur = alist
    visited = []
    while cur and cur not in visited:
        print(cur.val, end=', ')
        visited += cur,
        cur = cur.next
    print()



stime = time.time()
#print_cycle_list(Solution().insert(create_linked_list_from_nums([1]), 4))
print_cycle_list(Solution().insert(create_circular_linked_list_from_nums([30,50,2,2,3,5,7,9,11,20]), 2))
#print_cycle_list(Solution().insert(create_circular_linked_list_from_nums([3, 5, 1]), 4))
# print_cycle_list(Solution().insert(create_linked_list_from_nums([2, 2, 2]), 3))
print('elapse time: {} sec'.format(time.time() - stime))
