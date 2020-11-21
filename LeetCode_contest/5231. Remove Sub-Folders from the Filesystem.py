
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def removeSubfolders(self, folder: [str]) -> [str]:
        roots = []
        folder.sort(key=len)

        for path in folder:
            chunks = path.split('/')

            while chunks:
                if '/'.join(chunks) in roots:
                    break
                chunks.pop()
            else:
                roots += path,

        return roots




stime = time.time()
#print(["/a","/c/d","/c/f"] == Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(["/ah/al"] == Solution().removeSubfolders(["/ah/al/am","/ah/al"]))
print('elapse time: {} sec'.format(time.time() - stime))