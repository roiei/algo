import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ''
        s_idx = -1
        s_len = float('inf')
        for i in range(len(strs)):
            if s_len > len(strs[i]):
                s_len = len(strs[i])
                s_idx = i

        compare_set = strs[:s_idx]

        if s_idx+1 < len(strs):
            compare_set += strs[s_idx+1:]
        s_str = strs[s_idx]
        c_seq = ''

        while s_str:
            ncs = []
            common_exist = True
            for word in compare_set:
                found = False
                while word:
                    if word[0] != s_str[0]:
                        break
                    word = word[1:]
                    found = True
                    break
                ncs.append(word)
                if False == found:
                    common_exist = False
                    break
            compare_set = ncs
            if False == common_exist:
                break
            c_seq += s_str[0] 
            s_str = s_str[1:]
        return c_seq

    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ''

        cmm = ''
        n = min(len(str) for str in strs)

        for i in range(n):
            same = True
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    same = False
                    break

            if not same:
                break

            cmm += strs[0][i]

        return cmm

    def longestCommonPrefix(self, strs: List[str]) -> str:
        def find_common(s1, s2):
            m = len(s1)
            n = len(s2)
            i = j = 0
            cnt = 0

            while i < m and j < n:
                if s1[i] != s2[j]:
                    break
                i += 1
                j += 1
                cnt += 1

            return s1[:cnt]

        cmm = strs[0]
        for i in range(1, len(strs)):
            cmm = find_common(cmm, strs[i])

        return cmm


print('' == Solution().longestCommonPrefix(["dog","racecar","car"]))
print('fl' == Solution().longestCommonPrefix(["flower","flow","flight"]))
print('a' == Solution().longestCommonPrefix(["aa","ab"]))
