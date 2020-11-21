import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""
You are given a string s of even length consisting of digits from 0 to 9, 
and two integers a and b.

You can apply either of the following two operations 
any number of times and in any order on s:

Add a to all odd indices of s (0-indexed). 
Digits post 9 are cycled back to 0. 
For example, if s = "3456" and a = 5, s becomes "3951".

Rotate s to the right by b positions. 
For example, if s = "3456" and b = 1, s becomes "6345".

Return the lexicographically smallest string 
you can obtain by applying the above operations any number of times on s.

A string a is lexicographically smaller than a string b (of the same length) 
if in the first position where a and b differ, 
string a has a letter that appears earlier in the alphabet 
than the corresponding letter in b. For example, 
"0158" is lexicographically smaller than "0190" 
because the first position they differ is at the third letter, 
and '5' comes before '9'.
"""


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def do_even(cur, a):
            res = []
            for i in range(len(cur)):
                if i%2 == 0:
                    res += cur[i],
                else:
                    res += str(int(cur[i]) + a)[-1],
            return res

        def do_rotate(cur, a):
            n = len(cur)
            a %= n
            return cur[n - a:] + cur[:n - a]

        n = len(s)
        q = [list(s)]
        pre = mn = float('inf')
        done = set()

        while q:
            cur = q.pop(0)
            icur = int(''.join(cur))
            if icur in done:
                continue

            done.add(icur)
            res = do_even(cur, a)
            q += res,
            res = do_rotate(cur, b)
            q += res,

        print(min(done))
        res = str(min(done))
        if len(res) < n:
            res = (n - len(res))*'0' + res
        return res


stime = time.time()
print("2050" == Solution().findLexSmallestString(s = "5525", a = 9, b = 2))
print('elapse time: {} sec'.format(time.time() - stime))