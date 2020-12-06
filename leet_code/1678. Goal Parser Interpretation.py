import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def interpret(self, command: str) -> str:
        mapping = {
            'G': 'G',
            '()': 'o',
            '(al)': 'al'
        }

        res = ''
        i = 0
        while i < len(command):
            cmd = ''
            while i < len(command) and cmd not in mapping:
                cmd += command[i]
                i += 1

            res += mapping[cmd]

        return res


stime = time.time()
print("Goal" == Solution().interpret("G()(al)"))
print('elapse time: {} sec'.format(time.time() - stime))
