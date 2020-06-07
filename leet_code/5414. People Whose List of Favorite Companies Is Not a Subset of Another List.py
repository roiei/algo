
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def peopleIndexes(self, favoriteCompanies: [[str]]) -> [int]:
        uniq = collections.defaultdict(set)

        for i, comp in enumerate(favoriteCompanies):
            uniq[i] = set(comp)

        res = []

        for i in range(len(uniq)):
            for j in range(len(uniq)):
                if i == j:
                    continue

                if uniq[i] <= uniq[j]:
                    break
            else:
                res += i,

        return res


stime = time.time()
print([0,1] == Solution().peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
print('elapse time: {} sec'.format(time.time() - stime))