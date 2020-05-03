
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def displayTable(self, orders: [[str]]) -> [[str]]:
        kinds = set()
        tbls = collections.defaultdict(dict)
        
        for name, tbl, dish in orders:
            tbl = int(tbl)
            kinds.add(dish)
            if dish not in tbls[tbl]:
                tbls[tbl][dish] = 0
            tbls[tbl][dish] += 1
        
        tbls = sorted(tbls.items(), key=lambda p: p[0])
        lines = []
        kinds = sorted(list(kinds))
        
        for tbl, freq in tbls:
            line = []
            for kind in kinds:
                if kind in freq:
                    line += freq[kind],
                else:
                    line += 0,
            
            lines += list(map(str, [tbl] + line)),
        
        return [["Table"] + kinds] + lines


stime = time.time()
print( [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]  == Solution().displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
print('elapse time: {} sec'.format(time.time() - stime))