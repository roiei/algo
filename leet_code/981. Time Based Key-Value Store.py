
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class TimeMap:
    def __init__(self):
        self.data = {}
        
    def search(self, key, ts):
        l = 0
        r = len(self.data[key]) - 1
        
        while l <= r:
            m = (l + r)//2
            if self.data[key][m][0] == ts:
                return m
            if self.data[key][m][0] < ts:
                l = m + 1
            else:
                r = m - 1
        return l

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        
        self.data[key] += (timestamp, value),

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ''
        
        idx = bisect.bisect_left(self.data[key], (timestamp, ''))
        if idx > len(self.data[key]) - 1:
            idx = len(self.data[key]) - 1
        
        while idx > 0 and self.data[key][idx][0] > timestamp:
            idx -= 1
            
        if self.data[key][idx][0] <= timestamp:
            return self.data[key][idx][1]
        return ''
    

#["TimeMap","set","set","get","set","get","set","set","get","set","get","set","get","set","get","set","get","get","get","get","get","get","set","set","set","get","get","set","set","get","set"]

tcs = [["rtzoj","kuexwze",1],["xcywxndnz","herqmazp",2],["xcywxndnz",3],["rtzoj","dgpguflin",4],["xcywxndnz",5],["dgpguflin","lvrexco",6],["xcywxndnz","dgpguflin",7],["xcywxndnz",8],["rtzoj","wxqixmxs",9],["xcywxndnz",10],["kuexwze","lvrexco",11],["dgpguflin",12],["lvrexco","wxqixmxs",13],["xcywxndnz",14],["herqmazp","vjfhio",15],["dgpguflin",16],["herqmazp",17],["herqmazp",18],["rtzoj",19],["herqmazp",20],["herqmazp",21],["kuexwze","vjfhio",22],["dgpguflin","qrkihrb",23],["kuexwze","dgpguflin",24],["rtzoj",25],["dgpguflin",26],["herqmazp","rtzoj",27],["lvrexco","iztpo",28],["lvrexco",29],["kuexwze","lvrexco",30]]

output = [None,None,"herqmazp",None,"herqmazp",None,None,"dgpguflin",None,"dgpguflin",None,"lvrexco",None,"dgpguflin",None,"lvrexco","vjfhio","vjfhio","wxqixmxs","vjfhio","vjfhio",None,None,None,"wxqixmxs","qrkihrb",None,None,"iztpo",None]

stime = time.time()
tm = TimeMap()
res = []
for tc in tcs:
    if len(tc) == 3:
        res += tm.set(*tc),
    else:
        res += tm.get(*tc),
print(res == output)


#print("PINALSIGYAHRPI" == Solution().convert("PAYPALISHIRING", 4))
print('elapse time: {} sec'.format(time.time() - stime))