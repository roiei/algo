
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        
        def neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]:
                    break

            T = list(S)
            for j in range(i+1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    T[j], T[i] = T[i], T[j]

        queue = collections.deque([A])
        seen = {A: 0}
        
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)


    def kSimilarity(self, A: str, B: str) -> int:
        q = [(A, 0)]
        visited = set(A)

        while q:
            s, num = q.pop(0)
            if s == B:
                break

            for i in range(len(s)):
                if s[i] != B[i]:
                    break

            tmp = list(s)

            for j in range(i + 1, len(s)):
                if B[i] != s[j]:
                    continue

                tmp[i], tmp[j] = tmp[j], tmp[i]
                tmp_str = ''.join(tmp)
                if tmp_str not in visited:
                    q += (tmp_str, num + 1),
                    visited.add(tmp_str)

                tmp[i], tmp[j] = tmp[j], tmp[i]

        return num



stime = time.time()
print(2 == Solution().kSimilarity(A = "abac", B = "baca"))
print('elapse time: {} sec'.format(time.time() - stime))