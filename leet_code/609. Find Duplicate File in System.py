import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findDuplicate(self, paths: [str]) -> [[str]]:
        contents = collections.defaultdict(list)
        
        for path in paths:
            items = path.split()
            for i in range(1, len(items)):
                sidx_content = items[i].find('(')
                eidx_content = items[i].find(')')
                
                len_type = eidx_content - sidx_content - 1
                content_type = items[i][sidx_content + 1:eidx_content]
                contents[content_type] += items[0] + '/' + items[i][:sidx_content],
        
        contents = sorted(contents.items(), key=lambda p:p[0], reverse=True)
        res = []
        for k, v in contents:
            if len(v) > 1:
                res += v,

        return res


stime = time.time()
print([["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]] == Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
print([] == Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]))
print('elapse time: {} sec'.format(time.time() - stime))