
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class UndergroundSystem:
    def __init__(self):
        self.check_in = collections.defaultdict(list)
        self.check_out = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[stationName + 'in'] += (id, t),

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.check_out[stationName + 'out'] += (id, t),
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        inc = 0
        num = 0

        for sid, st in self.check_in[startStation + 'in']:
            for eid, et in self.check_out[endStation + 'out']:
                if sid == eid and et >= st:
                    inc += et - st
                    num += 1

        return inc/num


ins = zip(["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"], [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]], [None,None,None,None,None,None,None,14.0,11.0,None,11.0,None,12.0])

sys = None
for op, param, out in ins:
    ret = None
    if op == 'UndergroundSystem':
        sys = UndergroundSystem()
    elif op == 'checkIn':
        ret = sys.checkIn(*param)
    elif op == 'checkOut':
        ret = sys.checkOut(*param)
    elif op == 'getAverageTime':
        ret = sys.getAverageTime(*param)

    if ret != out:
        print('ERROR @ op {}, param = {}, ret = {}, out = {}'.format(op, param, ret, out))