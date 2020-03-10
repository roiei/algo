import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        if not employees:
            return 0
        
        graph = {}
        for emp in employees:
            if emp.id not in graph:
                graph[emp.id] = []
            graph[emp.id] =+ emp.importance,
            subs = []
            for sub in emp.subordinates:
                subs += sub,
            graph[emp.id] += subs,
        
        tot = 0
        q = [id]
        visit = set()
        while q:
            id = q.pop(0)
            tot += graph[id][0]
            for sub in graph[id][1]:
                if sub not in visit:
                    q += sub,
                    visit.add(sub)
        return tot

    def getImportance(self, employees, id):
        if not employees:
            return 0
        
        g = collections.defaultdict(list)
        w = collections.defaultdict(int)
        
        for emp in employees:
            w[emp.id] = emp.importance
            
            for subid in emp.subordinates:
                g[emp.id] += subid,
        
        imp = 0
        visit = set()
        q = [id]
        while q:
            id = q.pop()
            visit.add(id)
            imp += w[id]
            
            for adj in g[id]:
                if adj not in visit:
                    q += adj,
        
        return imp


stime = time.time()

print(Solution().getImportance([Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])], 1))
print('elapse time: {} sec'.format(time.time() - stime))


