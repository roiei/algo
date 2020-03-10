import time

class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class NestedIterator(object):
    def get_elems(self, li):
        if isinstance(li, NestedInteger):
            if None == li.getInteger():
                self.get_elems(li.getList())
            else:
                self.elems.append(li.getInteger())
                self.n+=1
        elif isinstance(li, list):
            for i in li:
                self.get_elems(i)

    def __init__(self, nestedList):
        self.n = 0
        self.elems = []
        for li in nestedList:
            self.get_elems(li)
        self.i = 0

    def next(self):
        if self.i < self.n:
            ret = self.elems[self.i]
            self.i += 1
            return ret
        return -1

    def hasNext(self):
        if self.i < self.n:
            return True
        return False

nestedList = [[1,1],2,[1,1]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)