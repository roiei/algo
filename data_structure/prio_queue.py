
class node:
    def __init__(self, name):
        self.name = name

class linkage:
    def __init__(self, snode, dnode, weight):
        self.snode  = snode
        self.dnode  = dnode
        self.weight = weight

class pqueue:
    def __init__(self):
        self.num = 0        # except root (no link)
        self.links = []
        pass

    def __deinit__(self):
        pass

    def insert(self, snode, dnode, weight):
        self.links.append(linkage(snode, dnode, weight))
        self.num += 1
        self.upheap()

    def print_all(self):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        for i in range(0, self.num):
            print('{} --{}--> {}'.format(self.links[i].snode.name, self.links[i].weight, self.links[i].dnode.name))
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    def __swap(self, lsrc, ldst):
        lsrc.snode, ldst.snode = ldst.snode, lsrc.snode
        lsrc.dnode, ldst.dnode = ldst.dnode, lsrc.dnode
        lsrc.weight, ldst.weight = ldst.weight, lsrc.weight

    def upheap(self):
        n = self.num - 1
        cur = self.links[n]
        while n > 0:
            par_idx = (n - 1)//2
            par = self.links[par_idx]
            #print('comparing..cur={}/{}, par={}/{}'.format(n, cur.weight, par_idx. par.weight))
            if cur.weight <= par.weight:
                break
            self.__swap(par, cur)
            cur = self.links[par_idx]
            n = par_idx

    def downheap(self, i):
        cur = self.links[i]
        while i < self.num // 2:
            chd_idx = 1 if i == 0 else ((i+1)*2 - 1)
            #print('chd_idx : ', chd_idx, ' max_num : ', self.num)
            if chd_idx+1 < self.num and self.links[chd_idx].weight < self.links[chd_idx+1].weight:
                chd_idx += 1
            if cur.weight < self.links[chd_idx].weight:
                self.__swap(cur, self.links[chd_idx])
            cur = self.links[chd_idx]
            i = chd_idx

    def extract(self):
        if self.num == 0:
            return None
        link = self.links[0]
        self.links[0] = self.links[self.num - 1]
        del self.links[self.num - 1]
        self.num -= 1
        if self.num > 0:
            self.downheap(0)
        return link

    def update(self, snode, dnode, weight):
        for l in self.links:
            #print('dnode={}/{}, new_node={}/{}'.format(l.dnode.name, l.weight, dnode.name, weight))
            if l.dnode.name == dnode.name and l.weight < weight:
                #print(' --> dnode={}/{}, new_node={}/{}'.format(l.dnode.name, l.weight, dnode.name, weight))
                l.snode = snode
                l.weight = weight
                for k in range((self.num - 1)//2, 1):
                    self.downheap(k)
                return True
        return False

    def empty(self):
        return True if self.num == 0 else False

    def is_link_exist(self, name_src, name_dst):
        found = False
        for link in self.links:
            if link.snode.name == name_src and link.dnode.name == name_dst:
                found = True
                break
        for link in self.links:
            if link.dnode.name == name_src and link.snode.name == name_dst:
                found = True
                break
        return found

def unit_test():
    pq = pqueue()
    pq.insert(node('1'), node('2'), 20)
    pq.insert(node('1'), node('3'), 10)
    pq.insert(node('2'), node('4'), 50)
    pq.insert(node('1'), node('2'), 60)
    pq.print_all()
    print()
    #print(pq.extract().weight)
    #pq.print_all()

    pq.update(node('2'), node('4'), 80)
    pq.print_all()