
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


















stime = time.time()
print("adbc" == Solution().smallestSubsequence("cdadabcc"))
print('elapse time: {} sec'.format(time.time() - stime))
