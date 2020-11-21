import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def get_val(self, depth, N, K, val):
        if depth == N:
            return val
        half = 2**((N-depth)-1)
        if K <= half:
            return self.get_val(depth+1, N, K, 0 if val == 0 else 1)
        else:
            return self.get_val(depth+1, N, K-half, 1 if val == 0 else 0)


    def kthGrammar(self, N: int, K: int) -> int:
        return self.get_val(1, N, K, 0)


    def kthGrammar(self, N: int, K: int) -> int:
        def dfs(word, depth):
            if (word, depth) in mem:
                return mem[(word, depth)]

            if depth == N - 2:
                if word == '0':
                    return '01'
                else:
                    return '10'

            ret = ''
            if word == '0':
                ret += dfs('0', depth + 1)
                ret += dfs('1', depth + 1)
            else:
                ret += dfs('1', depth + 1)
                ret += dfs('0', depth + 1)

            mem[(word, depth)] = ret
            return ret

        mem = {}

        if N < 2:
            word = '0'
        else:
            word = dfs('0', 0)

        return word[K - 1]


stime = time.time()
sol = Solution()
#print('0' == sol.kthGrammar(1, 1)) # 0
#print('0' == sol.kthGrammar(2, 1)) # 0 
#print('1' == sol.kthGrammar(2, 2)) # 1
#print('1' == sol.kthGrammar(4, 5)) # 1
#print('0' == sol.kthGrammar(3, 4)) # 0
print('0' == sol.kthGrammar(30, 434991989)) # 0
print('elapse time: {} sec'.format(time.time() - stime))