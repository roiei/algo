import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def getFolderNames(self, names: [str]) -> [str]:
        exists = set()
        last = collections.defaultdict(int)
        result = []

        for name in names:
            k = last[name]
            modified = name

            while modified in exists:
                k += 1
                modified = f'{name}({k})'

            last[name] = k
            result.append(modified)
            exists.add(modified)
            
        return result


stime = time.time()
# print(["pes","fifa","gta","pes(2019)"] == Solution().getFolderNames(names = ["pes","fifa","gta","pes(2019)"]))
print(["gta","gta(1)","gta(2)","avalon"] == Solution().getFolderNames(names = ["gta","gta(1)","gta","avalon"]))
# print(["wano","wano(1)","wano(2)","wano(3)"] == Solution().getFolderNames(["wano","wano","wano","wano"]))
print('elapse time: {} sec'.format(time.time() - stime))