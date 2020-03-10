import time
from util_list import *


class Solution:
    def get_path_min(self, triangle, n, depth, start, limit, trace):
        if n == depth:
            print('sum = ', sum(trace), trace)
            self.min_sum = min(self.min_sum, sum(trace))
            return
        for i in range(start, len(triangle[depth])):
            if i > limit:
                continue

            trace.append(triangle[depth][i])
            self.get_path_min(triangle, n, depth+1, i, i+1, trace)
            trace.pop()

    def minimumTotal_es(self, triangle: 'List[List[int]]') -> int:
        if not triangle:
            return 0
        self.min_sum = 0x7FFFFFFF
        self.trace = []
        self.get_path_min(triangle, len(triangle), depth=0, start=0, limit=1, trace=[])
        return self.min_sum

    def minimumTotal_topdown(self, triangle):
        for i in range(1, rows):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])

    def minimumTotal_bottomup(self, triangle: List[List[int]]) -> int:
        mat = triangle
        if len(mat) == 1:
            return mat[0][0]
        for row in range(len(mat)-2, -1, -1):
            for col in range(len(mat[row])):
                mat[row][col] += min(mat[row+1][col], mat[row+1][col+1])
        return mat[0][0]


stime = time.time()
print(Solution().minimumTotal_bottomup([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))

# print(Solution().minimumTotal([
#     [-1],
#     [2,3],
#     [1,-1,-3]]))

# print(Solution().minimumTotal([
#     [-1],
#     [3,2],
#     [-3,1,-1]]))

print('elapse time: {} sec'.format(time.time() - stime))