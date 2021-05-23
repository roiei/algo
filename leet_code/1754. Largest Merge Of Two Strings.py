import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def largestMerge(self, s1, s2):
        def dfs(s1, s2):
            if s1 and s2:
                if s1 >= s2:
                    return s1[0] + dfs(s1[1:], s2)

                if s2 >= s1:
                    return s2[0] + dfs(s1, s2[1:])
            elif s1:
                return s1[0] + dfs(s1[1:], s2)
            elif s2:
                return s2[0] + dfs(s1, s2[1:])
            return ''

        return dfs(s1, s2)

    def largestMerge(self, s1, s2):
        i = 0
        j = 0
        res = ''

        while i < len(s1) or j < len(s2):
            if i < len(s1) and j < len(s2):
                if s1[i:] >= s2[j:]:
                    res += s1[i]
                    i += 1

                if s2[j:] >= s1[i:]:
                    res += s2[j]
                    j += 1
            elif i < len(s1):
                res += s1[i]
                i += 1
            elif j < len(s2):
                res += s2[j]
                j += 1
            else:
                break

        return res


assert("cbcabaaaaa" == Solution().largestMerge("cabaa", "bcaaa"))