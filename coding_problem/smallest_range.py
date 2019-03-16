

import heapq


list1 = [4, 10, 15, 24, 26]
list2 = [0, 9, 12, 20]
list3 = [5, 18, 22, 30]

class DiffElem:
    def __init__(self, start, mid, end):
        self.start = start
        self.mid = mid
        self.end = end
        self.diff = end - start
    def __lt__(self, other):
        return self.diff < other.diff

def find_diff(l1, l2, l3, res):
    if not l1 or not l2 or not l3:
        return
    comp_elems = []
    comp_elems.extend([l1[0], l2[0], l3[0]])
    comp_elems = sorted(comp_elems)
    heapq.heappush(res, DiffElem(comp_elems[0], comp_elems[1], comp_elems[2]))
    if comp_elems[0] == l1[0]:
        find_diff(l1[1:], l2, l3, res)
    elif comp_elems[0] == l2[0]:
        find_diff(l1, l2[1:], l3, res)
    else:
        find_diff(l1, l2, l3[1:], res)

res = []
find_diff(list1, list2, list3, res)
while res:
    de = heapq.heappop(res)
    print('start:{:-3}, mid:{:-3}, end:{:-3}, diff:{:-3}'
        .format(de.start, de.mid, de.end, de.diff))

