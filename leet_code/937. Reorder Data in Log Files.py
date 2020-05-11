
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for log in logs:
            slog = log.split()
            id = slog[0]
            if slog[1][0].isalpha():
                letters += (' '.join(slog[1:]), id),
            else:
                digits += log,
        
        letters.sort()
        res = []
        for body, id in letters:
            res += id + ' ' + body,
        
        res += digits
        return res
        

stime = time.time()
print(["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"] == Solution().reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
print('elapse time: {} sec'.format(time.time() - stime))