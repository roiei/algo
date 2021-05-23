
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        opn = 0
        res = ''
        kwd = ''

        kwd_tbl = collections.defaultdict(str)
        for k, v in knowledge:
            kwd_tbl[k] = v

        for i in range(len(s)):
            if s[i] == '(':
                opn += 1
            elif s[i] == ')':
                opn -= 1

            if opn:
                kwd += s[i]
            elif kwd:
                kwd = kwd[1:]
                res += kwd_tbl[kwd] if kwd in kwd_tbl else '?'
                kwd = ''
            else:
                res += s[i]

        return res


stime = time.time()
print("yesyesyesaaa" == Solution().evaluate("(a)(a)(a)aaa", [["a","yes"]]))
print("hi?" == Solution().evaluate("hi(name)", [["a","b"]]))
print('elapse time: {} sec'.format(time.time() - stime))