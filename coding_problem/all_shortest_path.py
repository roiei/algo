


import queue
from edge import *


class Link:
    def __init__(self, v, w):   # v is dst
        self.v = v              # v is vertex
        self.w = w              # w is weight

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjlist = []
        self.visit = False
        self.distance = 0
        self.parent = 0

        # for topological sort
        self.indegree = 0
        self.outdegree = 0

    def find(self, v):
        for link in self.adjlist:
            if v.name == link.v.name:
                return True
        return False

    def add(self, v, w):
        if True == self.find(v):
            return False
        self.adjlist.append(Link(v, w))
        return True

    def __lt__(self, other):
        if self.name < other.name:
            return True
        return False

class Graph:
    def __init__(self, directed=False):
        self.vertices = []
        self.directed = directed
        pass

    def find(self, name):
        for v in self.vertices:
            if name == v.name:
                return v
        return None

    def add(self, v):
        self.vertices.append(v)

    def getVertex(self, name):
        v = self.find(name)
        if None == v:
            v = Vertex(name)
            self.add(v)
        return v

    def link(self, sname, dname, w):
        sv = self.getVertex(sname)
        dv = self.getVertex(dname)
        sv.add(dv, w)
        if self.directed == False:
            dv.add(sv, w)

    def clear_visit(self):
        for v in self.vertices:
            v.visit = False
            v.distance = 0

    def shortest_dijkstra(self, start_name):
        cur_v = self.find(start_name)
        if None == cur_v:
            return
        for v in self.vertices:
            v.visit    = False
            v.parent   = cur_v if v.name != start_name else None
            v.distance = 0                      # 0 == INF
        adj_max_dist = 0
        for adv_link in cur_v.adjlist:
            adv_link.v.distance = adv_link.w    # distance = edge's weight, at first
            if adj_max_dist < adv_link.w:
                adj_max_dist = adv_link.w + 1
        
        traq = queue.Queue()
        cur_v.distance = adj_max_dist
        cur_v.visit = True
        traq.put(cur_v)

        while not traq.empty():
            cur_v = traq.get()
            for v in self.vertices:
                if (v.visit == False 
                    and v.distance > 0 
                    and cur_v.distance > v.distance):

                    v.visit = True
                    traq.put(v)
                    for link in v.adjlist:
                        if link.v.visit == True:
                            continue
                        dist = v.distance + link.w
                        if link.v.distance == 0 or dist < link.v.distance:
                            link.v.distance = dist
                            link.v.parent = v

        # for v in self.vertices:
        #     if v.parent != None:
        #         print('{} -- {} --> {}'.format(v.parent.name, v.distance, v.name))


def set_links(g):
    g.link('5', '1', 1)
    g.link('1', '2', 2)
    g.link('1', '3', 3)
    g.link('2', '3', 4)
    g.link('2', '4', 5)
    g.link('3', '4', 6)

import sys

g = Graph()

num_v, num_e = map(int, input().split())
start = str(int(input()))
for i in range(num_e):
    v, u, w = map(int, sys.stdin.readline().split())
    g.link(str(v), str(u), w)


# start = '1'
# set_links(g)

g.shortest_dijkstra(start)

for i in range(len(g.vertices)):
    v = g.find(str(i+1))
    if None == v:
        break
    if v.name == start:
        print(0)
    elif 0 == v.distance:
        print('INF')
    else:
        print(v.distance)


