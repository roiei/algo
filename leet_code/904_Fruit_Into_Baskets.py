import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        if tree.count(0) + tree.count(1) == len(tree):
            return len(tree)
        if len(tree) < 1 or len(tree) > 40000:
            return 0
        if tree.count(0) == len(tree):
            return len(tree)
        lengths = []
        for i in range(len(tree)):
            length = 0
            bsk_kind = []
            for j in range(i, len(tree), 1):
                if tree[j] not in bsk_kind and len(bsk_kind) == 2:
                    break
                if tree[j] not in bsk_kind:
                    bsk_kind.append(tree[j])
                length += 1

            lengths.append(length)
        print(lengths)
        return max(lengths)


    def totalFruit(self, tree: [int]) -> int:
        wnd = []
        mcnt = cnt = 0
        pre = -1

        idx = collections.defaultdict(int)
        
        for i, t in enumerate(tree):
            if t not in wnd:
                if len(wnd) == 2:
                    wnd = [pre]
                    cnt = i - idx[pre]
                wnd += t,

            if pre != t:
                idx[t] = i

            cnt += 1
            mcnt = max(mcnt, cnt)
            pre = t
        
        return mcnt



stime = time.time()
print(3 == Solution().totalFruit([1, 2, 1]))
print(3 == Solution().totalFruit([0,1,2,2]))
print(4 == Solution().totalFruit([1,2,3,2,2]))
print(5 == Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
print(5 == Solution().totalFruit([1,0,1,4,1,4,1,2,3]))
print('elapse time: {} sec'.format(time.time() - stime))
