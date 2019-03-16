

import queue
from prio_queue import *
from edge import *
from Set import *


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

    def traverse(self, start_name):
        self.clear_visit()
        v = self.find(start_name)
        if None == v:
            return
        tq = []
        tq.append(v)
        v.visit = True
        while tq:
            v = tq.pop()
            print(v.name, end=' -> ')
            #print('----------------')
            for link in v.adjlist:
                #print('>> {}: {}'.format(v.name, link.v.name))
                adv = self.find(link.v.name)
                if False == adv.visit:
                    tq.append(adv)
                    adv.visit = True

    def bfs(self, start_name):
        self.clear_visit()
        v = self.find(start_name)
        if None == v:
            return
        tq = queue.Queue()
        tq.put(v)
        v.visit = True
        while not tq.empty():
            v = tq.get()
            print(v.name, end=' -> ')
            #print('----------------')
            for link in v.adjlist:
                #print('>> {}: {}'.format(v.name, link.v.name))
                adv = self.find(link.v.name)
                if False == adv.visit:
                    tq.put(adv)
                    adv.visit = True

    def pfs(self, start_name):  # MCST PFS
        self.clear_visit()
        v = self.find(start_name)
        if None == v:
            return
        acc = 0
        pq = pqueue()
        pq.insert(node(v.name), node(v.name), 0)    # the first one
        v.visit = True
        while not pq.empty():
            linkage = pq.extract()
            if linkage.snode.name != linkage.dnode.name:
                print('{} --{}--> {}'.format(linkage.snode.name, linkage.weight, linkage.dnode.name))
                acc += -linkage.weight

            d_vtx = self.find(linkage.dnode.name)    # target !!
            for link in d_vtx.adjlist:
                adv = self.find(link.v.name)
                if False == adv.visit:
                    pq.insert(node(d_vtx.name), node(adv.name), -link.w)
                    adv.visit = True
                else:
                    pq.update(node(d_vtx.name), node(adv.name), 
                        -link.w)
        return acc

    def MCST_Kruskal(self): # MCST Kruskal
        self.clear_visit()
        pq = pqueue()
        st = Set()
        for v in self.vertices:
            for link in v.adjlist:
                if True == pq.is_link_exist(v.name, link.v.name):
                    continue
                pq.insert(node(v.name), node(link.v.name), -link.w)
        acc = 0
        while not pq.empty():
            linkage = pq.extract()
            idx1 = st.find(linkage.snode.name)
            if -1 == idx1:
                idx1 = st.add(linkage.snode.name)
            idx2 = st.find(linkage.dnode.name)
            if -1 == idx2:
                idx2 = st.add(linkage.dnode.name)
            if idx1 >= 0 and idx2 >= 0 and idx1 != idx2:  # if more than or equal to one is inserted
                print('{} -- {} --> {}'.format(linkage.snode.name, linkage.weight, linkage.dnode.name))
                acc += -linkage.weight
                st.union_by_idx(idx1, idx2)
        return acc

    def find_shortest_pfs(self, start_name):  # shortest path PFS
        self.clear_visit()
        v = self.find(start_name)
        if None == v:
            return
        acc = 0
        pq = pqueue()
        pq.insert(node(v.name), node(v.name), 0)    # the first one
        v.visit = True
        while not pq.empty():
            linkage = pq.extract()
            if linkage.snode.name != linkage.dnode.name:
                print('{} --{}--> {}'.format(linkage.snode.name, linkage.weight, linkage.dnode.name))
                acc += -linkage.weight

            d_vtx = self.find(linkage.dnode.name)    # target !!
            for link in d_vtx.adjlist:
                adv = self.find(link.v.name)
                if False == adv.visit:
                    pq.insert(node(d_vtx.name), node(adv.name), linkage.weight - link.w)
                    adv.visit = True
                else:
                    pq.update(node(d_vtx.name), node(adv.name), linkage.weight - link.w)
        return acc

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

        for v in self.vertices:
            if v.parent != None:
                print('{} -- {} --> {}'.format(v.parent.name, v.distance, v.name))

    def reach_dfs(self, start_name):
        self.clear_visit()
        v = self.find(start_name)
        if None == v:
            return
        ts = []
        ts.append(v)
        v.visit = True
        while ts:
            v = ts.pop()
            print(v.name, end=' -> ')
            #print('----------------')
            for link in v.adjlist:
                #print('>> {}: {}'.format(v.name, link.v.name))
                adv = self.find(link.v.name)
                if False == adv.visit:
                    ts.append(adv)
                    adv.visit = True

    def get_vertex_idx(self, name):
        idx = 0
        for v in self.vertices:
            if v.name == name:
                break
            idx += 1
        return idx

    def _do_strong_connect(self, i, order, porder, stack):
        order += 1
        porder[i] = min = order
        stack.append(i)
        for edge in self.vertices[i].adjlist:
            k = self.get_vertex_idx(edge.v.name)
            if porder[k] == 0:
                m = self._do_strong_connect(k, order, porder, stack)
            else:
                m = porder[k]
            if m < min:
                min = m
        if min == porder[i]:    # itself
            cycle = False
            while True:
                k = stack.pop()
                if k == i:
                    break
                print(' -> ', self.vertices[k].name)
                porder[k] = len(self.vertices) + 1
                cycle = True
            if cycle == True:
                print('cycle : ', self.vertices[k].name)
        return min

    def do_strong_connect(self):
        stack = []
        porder = [0 for i in range(len(self.vertices))]
        for i in range(len(self.vertices)):
            if porder[i] == 0:
                self._do_strong_connect(i, 0, porder, stack)

    def do_topological_sort(self):
        for v in self.vertices:
            for link in v.adjlist:
                link.v.indegree += 1
        q = queue.Queue()
        for v in self.vertices:
            if v.indegree == 0:
                q.put(v)
        while not q.empty():
            cur = q.get()
            print(cur.name, ' -> ')
            for link in cur.adjlist:
                link.v.indegree -= 1
                if 0 == link.v.indegree:
                    q.put(link.v)

    def do_reverse_topological_sort(self):
        for v in self.vertices:
            v.outdegree = len(v.adjlist)
        q = queue.Queue()
        for v in self.vertices:
            if v.outdegree == 0:
                q.put(v)
        while not q.empty():
            cur = q.get()
            print(cur.name, ' -> ')
            for v in self.vertices:
                for link in v.adjlist:
                    if link.v.name == cur.name:
                        v.outdegree -= 1
                        if 0 == v.outdegree:
                            q.put(v)

            


def set_links(g):
    g.link('A', 'C', 1)
    g.link('A', 'B', 4)
    g.link('A', 'D', 2)
    g.link('A', 'E', 3)
    g.link('C', 'D', 2)
    g.link('D', 'F', 4)
    g.link('B', 'F', 4)
    g.link('E', 'F', 4)
    g.link('D', 'G', 4)
    g.link('G', 'H', 3)
    g.link('G', 'I', 3)
    g.link('G', 'J', 4)
    g.link('H', 'I', 2)
    g.link('I', 'J', 2)
    g.link('F', 'J', 2)
    g.link('J', 'K', 1)
    g.link('F', 'K', 4)

def set_links_directed(g):
    g.link('A', 'C', 1)
    g.link('A', 'B', 4)
    g.link('A', 'D', 2)
    g.link('E', 'A', 3)
    g.link('D', 'C', 2)
    g.link('D', 'F', 4)
    g.link('F', 'D', 4)
    g.link('F', 'B', 4)
    g.link('F', 'E', 4)
    g.link('G', 'D', 4)
    g.link('H', 'G', 3)
    g.link('I', 'G', 3)
    g.link('G', 'J', 4)
    g.link('H', 'I', 2)
    g.link('J', 'I', 2)
    g.link('J', 'F', 2)
    g.link('J', 'K', 1)
    g.link('K', 'F', 4)

def set_topological_sort(g):
    g.link('A', 'B', 1)
    g.link('B', 'C', 1)
    g.link('C', 'D', 1)
    g.link('C', 'E', 1)
    g.link('C', 'F', 1)
    g.link('C', 'G', 1)
    g.link('E', 'K', 1)
    g.link('F', 'H', 1)
    g.link('F', 'I', 1)
    g.link('F', 'J', 1)
    g.link('H', 'K', 1)
    g.link('I', 'K', 1)
    g.link('J', 'K', 1)
    g.link('K', 'L', 1)

def unit_test_undirected_g():
    g = Graph()
    set_links(g)
    
    # g.traverse('A')
    # print()
    # g.bfs('A')

    #print(g.MCST_Kruskal())
    #print(g.pfs('A'))
    print(g.find_shortest_pfs('A'))
    g.shortest_dijkstra('A')
    
    #g.pfs2('A')


def unit_test_directed_g():
    g = Graph(True)

    # 
    #set_links_directed(g)
    #g.reach_dfs('A')
    #g.do_strong_connect()

    # topological
    set_topological_sort(g)
    g.do_topological_sort()
    print()
    g.do_reverse_topological_sort()


unit_test_undirected_g()
#unit_test_directed_g()
