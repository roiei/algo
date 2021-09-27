import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        infos = collections.defaultdict(list)
        filtered = []
        
        for item in transactions:
            name, time, amount, city = item.split(',')
            time = int(time)
            amount = int(amount)
            
            if amount > 1000:
                filtered += (name, time, amount, city),
                continue
                
            infos[name] += (time, amount, city),
        
        for k in infos.keys():
            infos[k].sort(key=lambda p: p[0])
            cur_infos = infos[k]
            
            stk = [cur_infos.pop(0)]

            while cur_infos:
                while stk and stk[-1][2] != cur_infos[0][2] \
                    and stk[-1][0] + 60 >= cur_infos[0][0]:

                    filtered. add((k, *stk.pop()))
                    filtered.add((k, *cur_infos[0]))

                stk += cur_infos.pop(0),
        
        res = []
        for item in filtered:
            name, time, amount, city = item
            res += (name, time, amount, city),

        res.sort(key=lambda p: p[1])
        res = ['{},{},{},{}'.format(*item) for item in res]

        print(res)
        return res

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        items = sorted([i.split(",") for i in transactions], 
            key=lambda p:(p[0], int(p[1])))

        n = len(items)
        added = set()
        res = []
        
        for i, trans in enumerate(items):
            j = i + 1
            fraud = False
            while j < n and items[j][0] == trans[0] and int(trans[1]) + 60 >= int(items[j][1]):
                if trans[3] != items[j][3]:
                    fraud = True
                j += 1    
            
            k = i
            while fraud and k < j:
                if k not in added:
                    added.add(k)
                    res += ",".join(items[k]),
                k += 1
            
            if int(trans[2]) > 1000 and i not in added:
                added.add(i)
                res += ",".join(trans),
                
        return res


stime = time.time()
print(["alice,20,800,mtv","alice,50,100,beijing"] == Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))
print(["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"] == Solution().invalidTransactions(
    ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]))
print('elapse time: {} sec'.format(time.time() - stime))
