import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def longestPalindrome(self, s):
        length = 0
        elems = collections.Counter(s)

        for ch, cnt in elems.items():            
            if 0 == cnt%2:
              even = cnt
            else:
              even = (cnt//2)*2

            left = cnt - even
            length += even

            if 0 == length%2:
                length += left

        return length

    def longestPalindrome(self, s):
        n = len(s) + 1
        tbl = [[0]*n for _ in range(n)]

        rs = s[::-1]

        for i in range(n - 1):
            for j in range(n - 1):
                if s[i] == rs[j]:
                    tbl[i + 1][j + 1] = \
                        max(tbl[i][j] + 1, 
                            tbl[i][j + 1],
                            tbl[i + 1][j])
                else:
                    tbl[i + 1][j + 1] = \
                        max(tbl[i][j], 
                            tbl[i][j + 1],
                            tbl[i + 1][j])

        return tbl[-1][-1]

    def longestPalindrome(self, s):
        # O(2^N)

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in mem:
                return mem[(l, r)]

            score = 0
            if l < r and s[l] == s[r]:
                score += dfs(l + 1, r - 1) + 2
            elif l == r:
                score += dfs(l + 1, r - 1) + 1
            else:
                score += max(dfs(l, r - 1), dfs(l + 1, r))

            mem[(l, r)] = score
            return score

        mem = {}
        return dfs(0, len(s) - 1)

    def longestPalindrome(self, s):
        cost_matrix = [[None]*len(s) for _ in range(len(s))]

        def get_cost(i, j):
            if i == j:
                return 1

            elif i > j:
                return 0

            if cost_matrix[i][j]:
                return cost_matrix[i][j]

            if s[i] == s[j]:
                cost_matrix[i][j] = get_cost(i + 1, j - 1) + 2
            else:
                cost_matrix[i][j] = \
                    max(get_cost(i, j - 1), 
                        get_cost(i + 1, j))

            return cost_matrix[i][j]

        return get_cost(0, len(s) - 1)



# print(collections.Counter([1, 2, 3, 4, 5, 6, 7, 3, 5, 7, 7]))
# print(collections.Counter('This is excellent Python package collections'))
# print(collections.Counter('this is Python and this Python is powerful'.split()))



stime = time.time()
#print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
# print(0 == Solution().longestPalindrome(""))
# print(1 == Solution().longestPalindrome("ab"))
# print(2 == Solution().longestPalindrome("aa"))
print(3 == Solution().longestPalindrome("animal"))

# print(7 == Solution().longestPalindrome("abccccdd"))
print('elapse time: {} sec'.format(time.time() - stime))
