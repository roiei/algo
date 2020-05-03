
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def stringMatching(self, words: [str]) -> [str]:
        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                idx = words[j].find(words[i])
                if -1 != idx:
                    res += words[i],
                    break

        return res


stime = time.time()
print(["as","hero"] == Solution().stringMatching(words = ["mass","as","hero","superhero"]))
print('elapse time: {} sec'.format(time.time() - stime))