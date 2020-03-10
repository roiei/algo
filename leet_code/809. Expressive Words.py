
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def expressiveWords(self, S: str, words: [str]) -> int:
        
        def get_uniq(S):
            src = []
            done = []
            s_cnt = collections.Counter(S)

            for ch in S:
                if ch not in done:
                    if s_cnt[ch] > 2:
                        src += (ch, (s_cnt[ch] - 2)%3),
                    else:
                        src += (ch, s_cnt[ch]),
                    done += ch,
            return src

        src = get_uniq(S)
        print(src)
        print()

        cnt = 0
        for word in words:
            tgt = get_uniq(word)
            #print('word = ', word, tgt)
            print(tgt)
            if src == tgt:
                cnt += 1

        return cnt


        





stime = time.time()
print(1 == Solution().expressiveWords(S = "heeellooo", words = ["hello", "hi", "helo"]))
print('elapse time: {} sec'.format(time.time() - stime))