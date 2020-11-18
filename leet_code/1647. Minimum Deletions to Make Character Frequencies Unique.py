import collections
import heapq


"""
A string s is called good if there are no two different characters in s 
that have the same frequency.

Given a string s, return the minimum number of characters 
you need to delete to make s good.

The frequency of a character in a string is the number of times 
it appears in the string. 

For example, in the string "aab", the frequency of 'a' is 2, 
while the frequency of 'b' is 1.


it is okay about freq is 0
1. get frequencies
2. for the same frequencies, decrease one except the first one
2.1 discard ones with the zero frequency
3. repeat
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        freq = collections.Counter(s)
        q = []
        for k, v in freq.items():
            heapq.heappush(q, (-v, k))

        res = []
        cnt = 0

        while q:
            prev = heapq.heappop(q)
            if not q:
                break
            cur = heapq.heappop(q)
            temp = []

            while q and prev[0] == cur[0]:
                if cur[0] != 0:
                    temp += cur,
                cur = heapq.heappop(q)

            if prev[0] == cur[0]:
                if cur[0] != 0:
                    temp += cur,
            else:
                heapq.heappush(q, cur)

            while temp:
                t = temp.pop()
                t = (t[0] + 1, t[1])
                heapq.heappush(q, t)
                cnt += 1

        return cnt


# c:1 e:1 a:1
# c:1 e:1 a:0
# c:1 e:0 a:0

# print(0 == Solution().minDeletions("aab"))
# print(2 == Solution().minDeletions("aaabbbcc"))
# print(2 == Solution().minDeletions("ceabaacb"))
# print(3 == Solution().minDeletions("abcabc"))
# print(2 == Solution().minDeletions("bbcebab"))
print(3 == Solution().minDeletions("adec"))


"""
    a:3, b:3, c:2
        a:3 -> 2
    b:3 a:2 c:2
        a:2 -> 1
    b:3 a:1 c:2

    same max count -> dec.

    a:3 c:2 b:2 e:1
    a:2 c:2 b:1 e:1
    a:2 c:2 b:1 e:0
    ...
"""