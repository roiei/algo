import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent


def search(order, name):
    i = 0
    while i < len(order):
        if order[i].name == name:
            return i
        i += 1
    
    return -1

        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.order = [Node(kingName, None)]
        
    def birth(self, parentName: str, childName: str) -> None:
        idx = search(self.order, parentName)
        idx += 1
        
        while idx < len(self.order) and self.order[idx].parent == parentName:
            idx += 1

        print(parentName, childName)
        print(idx, [item.name for item in self.order])
        
        self.order.insert(idx, Node(childName, parentName))
        print([item.name for item in self.order])
        print()

    def death(self, name: str) -> None:
        idx = search(self.order, name)
        self.order.pop(idx)  

    def getInheritanceOrder(self) -> [str]:
        return [item.name for item in self.order]
         

ins = zip(["ThroneInheritance","getInheritanceOrder","birth","birth","birth","birth","getInheritanceOrder","birth","getInheritanceOrder"], 
[["king"],[None],["king","clyde"],["clyde","shannon"],["shannon","scott"],["king","keith"],[None],["clyde","joseph"],[None]],
[None,["king"],None,None,None,None,["king","clyde","shannon","scott","keith"],None,["king","clyde","shannon","scott","joseph","keith"]])

ti = None
for op, param, ret in ins:
    res = None
    if op == 'ThroneInheritance':
        ti = ThroneInheritance(*param)
    elif op == 'getInheritanceOrder':
        res = ti.getInheritanceOrder()
    elif op == 'birth':
        res = ti.birth(*param)
    elif op == 'death':
        res = ti.death(*param)

    if ret != res:
        print('ERROR: ' + op + '(' + str(param) + ')' + ' -> ')
        print('ret = ', str(ret))
        print('res = ', res)


