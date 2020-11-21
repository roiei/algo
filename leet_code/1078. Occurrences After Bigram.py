import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        if len(text) < 2:
            return []

        wnd = []
        wnd += text[0],
        wnd += text[1],
        res = []
        
        for i in range(2, len(text)):
            if wnd[0] == first and wnd[1] == second:
                res += text[i],
            
            wnd.pop(0)
            wnd += text[i],
        
        return res


stime = time.time()
print(["girl","student"] == Solution().findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good"))
print('elapse time: {} sec'.format(time.time() - stime))