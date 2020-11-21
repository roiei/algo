
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def smallestSubsequence(self, text: str) -> str:
        res = []
        cnt = collections.Counter(text)
        seen = set()

        for ch in text:
            print('ch = ', ch, seen, res)
            cnt[ch] -= 1
            if ch not in seen:
                seen.add(ch)

                if res:
                    print('ch = ', ch, ' res[-1] = ', res[-1])
                while res and cnt[res[-1]] >= 1 and ch < res[-1]:
                    seen.remove(res.pop())
                res += ch,
                print(res)

            print()

        return ''.join(res)
            
            # "cdadabcc"
            #     c -> c
            #     d -> cd
            #     a -> a
            #     d -> ad
            #     a -> ...
            #     b -> 
            #     c -> ...
            # "adbc"

    def smallestSubsequence(self, text: str) -> str:
        s = text
        kind = sorted(list(set(s)))
        s = list(s)
        res = ''

        while kind:
            ch = kind.pop(0)
            print(ch)
            idx = s.index(ch)
            
            not_find = False
            for i in range(idx):
                if s[i] not in s[i + 1:]:
                    not_find = True
                    break
            
            if not not_find:
                res += ch
                s = s[idx + 1:]

                while s and ch in s:
                    s.remove(ch)

                kind = sorted(list(set(s)))

            print(res)
            print()

        return res


stime = time.time()
print("abc" == Solution().smallestSubsequence("bcabc"))
print("adbc" == Solution().smallestSubsequence("cdadabcc"))
print('elapse time: {} sec'.format(time.time() - stime))
