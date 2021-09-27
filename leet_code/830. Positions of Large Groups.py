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

    def largeGroupPositions(self, S: str):
        pre = -1
        pre_pos = -1
        cnt = 1
        res = []

        for i, ch in enumerate(S):
            if pre != ch:
                if cnt >= 3:
                    res += [pre_pos, i - 1],
                pre = ch
                pre_pos = i
                cnt = 1
            else:
                cnt += 1

        if cnt >= 3:
            res += [pre_pos, i],

        return res


stime = time.time()
# print([[3, 6]] == Solution().largeGroupPositions("abbxxxxzzy"))
print([] == Solution().largeGroupPositions("abc"))
print([[3,5],[6,9],[12,14]] == Solution().largeGroupPositions("abcdddeeeeaabbbcd"))
print([[0, 2]] == Solution().largeGroupPositions("aaa"))
print('elapse time: {} sec'.format(time.time() - stime))