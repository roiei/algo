
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        srcs = []
        node = head
        src_nodes = []

        while node:
            src_nodes += node,
            srcs += [node.val, None],
            node = node.next

        for i, node in enumerate(src_nodes):
            if node.random in src_nodes:
                idx = src_nodes.index(node.random)	# None is not in list
                srcs[i][1] = src_nodes[idx]


        dst_head = dst = Node(srcs[0][0], None, None)
        dst_nodes = [dst]

        for i in range(1, len(srcs)):
            dst.next = Node(srcs[i][0], None, None)
            dst = dst.next
            dst_nodes += dst,

        node = dst_head

        for i in range(len(srcs)):
            if src_nodes[i]:
                if src_nodes[i].random:
                    idx = src_nodes.index(src_nodes[i].random)
                    node.random = dst_nodes[idx]
            node = node.next

        return dst_head
            
            
stime = time.time()
print(3 == Solution().copyRandomList(create_linked_list_from_nums()))


print('elapse time: {} sec'.format(time.time() - stime))