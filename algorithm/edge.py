

import heapq

import queue


class Edge:
    def __init__(self, sname, dname, w):
        self.sname = sname
        self.dname = dname
        self.w     = w

    def __lt__(self, other):
        return self.w < other.w

    def ___le__(self, other):
        return self.w <= other.w

    def __eq__(self, other):
        return self.w == other.w

    def __ne__(self, other):
        return self.w != other.w

    def __gt__(self, other):
        return self.w > other.w

    def __ge__(self, other):
        return self.w >= other.w

def test_edge():
    q = queue.PriorityQueue()
    q.put(Edge('A', 10))
    q.put(Edge('B', 1))
    q.put(Edge('C', 5))

    while not q.empty():
        print(q.get().name)
    print()


