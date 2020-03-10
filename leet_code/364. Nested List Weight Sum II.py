
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution:
    """
    @param nestedList: a list of NestedInteger
    @return: the sum
    """
    def depthSumInverse(self, nestedList):
        if not nestedList:
            return 0

        def get_depth(obj, depth):
            if type(obj) != list:
                if obj.isInteger():
                    return depth
                else:
                    obj = obj.getList()
            
            deps = []
            for item in obj:
                deps += get_depth(item, depth + 1),
            
            return max(deps) if deps else 0
            
        depth = get_depth(nestedList, 0)
        if 0 == depth:
            return

        def do(obj, depth):
            res = 0
            if type(obj) != list:
                if obj.isInteger():
                    return depth*obj.getInteger()
                else:
                    obj = obj.getList()
            
            for item in obj:
                ret = do(item, depth - 1)
                if ret:
                    res += ret
            
            return res
        
        return do(nestedList, depth + 1)


stime = time.time()
print('elapse time: {} sec'.format(time.time() - stime))