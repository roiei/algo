import time


class Solution:
    def largeGroupPositions(self, S: str):
        if not S:
            return []
        prev = '@'
        start = 0
        res = []
        for i in range(len(S)):
            if prev != S[i]:
                if i-start >= 3:
                    res.append([start, i-1])
                start = i
            prev = S[i]
        if start != i and i-start >= 2:
            res.append([start, i])
        return res



stime = time.time()
# print([[3, 6]] == Solution().largeGroupPositions("abbxxxxzzy"))
print([] == Solution().largeGroupPositions("abc"))
print([[3,5],[6,9],[12,14]] == Solution().largeGroupPositions("abcdddeeeeaabbbcd"))
print([[0, 2]] == Solution().largeGroupPositions("aaa"))
print('elapse time: {} sec'.format(time.time() - stime))