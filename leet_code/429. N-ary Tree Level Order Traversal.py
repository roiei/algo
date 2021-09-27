import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        if not root:
            return []
        q = [root]
        trace = []
        while q:
            nq = []
            t = []
            while q:
                cur = q.pop(0)
                t.append(cur.val)
                for child in cur.children:
                    nq.append(child)
            trace.append(t)
            q = nq
        return trace

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        q = [root]

        while q:
            nq = []
            seq = []

            while q:
                node = q.pop(0)
                if not node:
                    continue

                seq += node.val,

                for child in node.children:
                    nq += child,

            q = nq
            if seq:
                res += seq,

        return res

