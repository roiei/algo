
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


# Given a string s and an array of integers cost 
# where cost[i] is the cost of deleting the character i in s.

# Return the minimum cost of deletions 
# such that there are no two identical letters next to each other.
 
# Notice that you will delete the chosen characters at the same time, 
# in other words, after deleting a character, 
# the costs of deleting other characters will not change.


    # 1  2  3  4  5
    # a  b  a  a  c   <- delete a (+3)

    # 1  2  4  5
    # a  b  a  c 


    # 1  2  3  4  1
    # a  a  b  a  a   <- delete the first a(+1)

    # 2  3  4  1
    # a  b  a  a      <- delete the last a(+1)



class Solution:
    def minCost(self, s: str, cost: [int]) -> int:
        class Elem:
            def __init__(self, ch, cost):
                self.ch = ch
                self.cost = cost

            def __str__(self):
                return self.ch

        def dfs(s, price):
            #print(''.join([elem.ch for elem in s]))
            key = ''.join([str((elem.ch, elem.cost)) for elem in s])
            if (key, price) in mem:
                return mem[(key, price)]
            res = None

            for i in range(len(s)):
                if i + 1 < len(s) and s[i].ch == s[i + 1].ch:
                    sub_inc = min(dfs(s[:i] + s[i + 1:], s[i].cost),
                        dfs(s[:i + 1] + s[i + 2:], s[i + 1].cost))

                    if res == None:
                        res = sub_inc
                    else:
                        res = min(res, sub_inc)

            res = 0 if res == None else res
            mem[(key, price)] = price + res
            return price + res

        elems = []
        for ch, price in zip(list(s), cost):
            elems += Elem(ch, price),

        mem = {}
        res = dfs(elems, 0)
        print(res)
        return res

    def minCost(self, s, cost):
        res = mx = 0

        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                mx = 0
            res += min(mx, cost[i])
            mx = max(mx, cost[i])

        return res



    1  2  3  4  5
    a  b  a  a  c
    ----
    mx = 0
    res += min(0, 2) -> += 0
    mx = max(0, 2) -> 2

    1  2  3  4  5
    a  b  a  a  c
       ----
    mx = 0
    res += min(0, 3) -> += 0
    mx = max(0, 3) -> 3

    1  2  3  4  5
    a  b  a  a  c
          ----
    mx = 3 <- keep the previous mx if the same values
    res += min(3, 4) -> += 3
    mx = max(3, 4) -> 4


    3  5  10  7  5  3  5  5  4  8  1
    a  a  a   b  b  b  a  b  b  b  b
    ----      ----        ----
    3            5           4
       ----      ----        ----
       5            3        5      <-- 5가 되려면, 이전 mx인 5와 max 결정 필요
                                        다르면 이전 mx는 0 하여 cost 계산

                                        mx는 현재 값으로 계속 갱신

    5   4   8
    a   a   a  이 경우, 
    -----
        5와 4에서는 4를 취해야 함
        pre mx가 5였을 시, 4 보다 크기에 5 값 유지

        즉, pre_mx는 현재 이전의 값 중 mx


    5   8
    a   a
    -----
        값을 5와 8에서 min을 취해야 함


    tot = mx = 0
    for i in range(len(s)):
        if i > 0 and s[i] != s[i - 1]:
            mx = 0

        tot += min(mx, cost[i])
        mx = max(mx, cost[i])

    return tot





stime = time.time()
print(3 == Solution().minCost(s = "abaac", cost = [1,2,3,4,5]))
print(0 == Solution().minCost(s = "abc", cost = [1,2,3]))
print(2 == Solution().minCost(s = "aabaa", cost = [1,2,3,4,1]))
print(26 == Solution().minCost("aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1]))
print('elapse time: {} sec'.format(time.time() - stime))