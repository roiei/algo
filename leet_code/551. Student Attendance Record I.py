import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def checkRecord(self, s: str) -> bool:
        if '' == s:
            return True
        rec = {'A':0, 'L':0, 'P':0}
        mcont_late = cont_late = 0
        for letter in s:
            if letter == 'L':
                cont_late += 1
                mcont_late = max(mcont_late, cont_late)
            else:
                cont_late = 0
            rec[letter] += 1
        mcont_late = max(mcont_late, cont_late)
        if rec['A'] > 1 or mcont_late > 2:
            return False
        return True



stime = time.time()
print("husband" == Solution().checkRecord("PPALLP"))
print('elapse time: {} sec'.format(time.time() - stime))