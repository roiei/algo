import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    # O(N^2logN) -> timeout
    def longestDupSubstring(self, S: str) -> str:
        def get_lcp(s1, s2):
            m = len(s1)
            n = len(s2)
            i = j = 0
            cnt = 0

            while i < m and j < n and s1[i] == s2[j]:
                cnt += 1
                i += 1
                j += 1

            return cnt

        mx = 0
        arr = []
        n = len(S)

        # 1. suffix array
        for i in range(n):
            arr += S[i:],

        arr.sort()
        res = ''

        # 2. LCP (Longest Common Prefix)
        for i in range(len(arr)):
            if i == 0:
                continue

            length = get_lcp(arr[i], arr[i - 1])
            if mx < length:
                res = arr[i][:length]
                mx = length

        return res


    # timeout
    def longestDupSubstring(self, S: str) -> str:
        class TrieNode:
            def __init__(self, ch):
                self.eow = False
                self.ch = ch
                self.child = {}

        def add(root, word) -> 'lcp':
            if not word:
                return

            one_way = True
            len_exist = 0
            trace = ''

            node = root
            for ch in word:
                if ch not in node.child:
                    node.child[ch] = TrieNode(ch)
                    one_way = False
                elif one_way:
                    trace += ch
                    len_exist += 1

                node = node.child[ch]

            node.eow = True
            return len_exist, trace

        root = TrieNode(None)
        mx = 0
        ret = ""

        for i in range(len(S)):
            l, t = add(root, S[i:])
            if mx < l:
                ret = t
                mx = l

        return ret

    def longestDupSubstring(self, S):
        N = len(S)
    
        class TrieNode:
            def __init__(self, start, depth):
                self.start = start
                self.depth = depth
                self.children = None;

            def index(self, start):
                ch  = S[start + self.depth]
                return string.ascii_lowercase.index(ch)

            def addNew(self, newStart):
                start, depth = self.start, self.depth
                if newStart + depth == N:
                    return depth

                if not self.children:
                    self.children = [0] * 26
                    index = self.index(start)
                    self.children[index] = TrieNode(start, depth + 1)

                childIndex = self.index(newStart)
                child = self.children[childIndex]
                if not child:
                    self.children[childIndex] = TrieNode(newStart, depth + 1)
                    return depth
                return child.addNew(newStart)

        start, length = 0, 0
        root = TrieNode(0, 0)
        i = 1
        while i + length < N:
            k = root.addNew(i)
            if k > length:
                length = k
                start = i
            i += 1
        return S[start : start + length]


stime = time.time()
print("" == Solution().longestDupSubstring("abcd"))
#print("ana" == Solution().longestDupSubstring("banana"))
print('elapse time: {} sec'.format(time.time() - stime))