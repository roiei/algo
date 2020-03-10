
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.i = self.n = 0
        self.data = []
        for vec in vec2d:
            self.data += vec
            self.n += len(vec)
        

    # @return {int} a next element
    def next(self):
        ret = self.data[self.i]
        self.i += 1
        return ret
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        return self.i < self.n


