
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache

"""
Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

If an element is the smallest element in its row and column, then its rank is 1.
If two elements p and q are in the same row or column, then:
If p < q then rank(p) < rank(q)
If p == q then rank(p) == rank(q)
If p > q then rank(p) > rank(q)
The rank should be as small as possible.
It is guaranteed that answer is unique under the given rules.



Input: matrix = [[1,2],
                 [3,4]]
Output: [[1,2],
         [2,3]]
Explanation:
The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.



Input: matrix = 
    [[ 20, -21, 14],
     [-19,   4, 19],
     [ 22, -47, 24],
     [-19,   4, 19]]

     -47        -21       4 
     X  X  X    X  2  X   ...
     X  X  X    X  X  X
     X  1  X    X  1  X
     X  X  X    X  X  X

     -47: (2, 1)            rows: [(2, 1)],         cols: [(1, 1)]
     -21: (0, 1)            rows: [(2, 1), (0, 2)], cols: [(1, 1), (1, 2)]
       4: (1, 1), (3, 1)    ...
       ...

Output: [
    [4,2,3],
    [1,3,4],
    [5,1,6],
    [1,3,4]]
"""


class Solution:
    def matrixRankTransform(self, matrix: [[int]]) -> [[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = [[0]*cols for _ in range(rows)]
        svals = []
        for y in range(rows):
            for x in range(cols):
                svals += (matrix[y][x], y, x),

        svals.sort(key=lambda p: p[0])
        vald = collections.defaultdict(list)

        for val, y, x in svals:
            vald[val] += (y, x),

        vert_rank = collections.defaultdict(int)
        vert_mx = collections.defaultdict(lambda: float('-inf'))
        hori_rank = collections.defaultdict(int)
        hori_mx = collections.defaultdict(lambda: float('-inf'))

        svals = list(set([val for val, y, x in svals]))
        svals.sort()

        print(svals)

        for val in svals:
            if val == 47:
                for line in ans:
                    print(line)
                print()
            rank = 1
            v_update = []
            h_update = []
            mx_rank = 1

            for y, x in vald[val]:
                rank = max(vert_rank[y], hori_rank[x]) + 1
                ans[y][x] = rank

            for y, x in vald[val]:
                ans[y][x] = rank
                vert_rank[y] = rank
                hori_rank[x] = rank


        for line in ans:
            print(line)
        return ans

    def matrixRankTransform(self, matrix):
        n, m = len(matrix), len(matrix[0])
        rank = [0] * (m + n)

        dvals = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                dvals[matrix[i][j]].append([i, j])

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        for val in sorted(dvals):
            p = list(range(m + n))
            rank2 = rank[:]

            for i, j in dvals[val]:
                i, j = find(i), find(j + n)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])

            for i, j in dvals[val]:
                rank[i] = rank[j + n] = matrix[i][j] = rank2[find(i)] + 1

    def matrixRankTransform(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        ans = [[0]*cols for _ in range(rows)]
        coords = collections.defaultdict(list)
        
        for y in range(rows):
            for x in range(cols):
                coords[matrix[y][x]] += (y, x),

        ranks = [0]*(rows + cols)
        uniq_vals = sorted(coords)

        def find(aset, val):
            if aset[val] != val:
                aset[val] = find(aset, aset[val])
            return aset[val]

        for val in uniq_vals:
            aset = list(range(rows + cols))
            tmp_ranks = collections.defaultdict(int)

            for y, x in coords[val]:
                y_root = find(aset, y)
                x_root = find(aset, x + rows)

                aset[y_root] = x_root
                tmp_ranks[x_root] = max(ranks[y_root], ranks[x_root], 
                    tmp_ranks[y_root], tmp_ranks[x_root])

            for y, x in coords[val]:
                ranks[y] = ranks[x + rows] = ans[y][x] = tmp_ranks[find(aset, y)] + 1

        return ans


stime = time.time()
print([[1,2],[2,3]] == Solution().matrixRankTransform([[1,2],[3,4]]))
print([[1,1],[1,1]] == Solution().matrixRankTransform([[7,7],[7,7]]))

# print(Solution().matrixRankTransform([[1,  2,  3],
# [1,  4,  1],
# [6,  7,  5]]))

print([[5,1,4],[1,2,3],[6,3,1]] == Solution().matrixRankTransform([[7,3,6],[1,4,5],[9,8,2]]))
print([[4,2,3],[1,3,4],[5,1,6],[1,3,4]] == Solution().matrixRankTransform([[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]))
print([[2,1,4,6],[2,6,5,4],[5,2,4,3],[4,3,1,5]] == Solution().matrixRankTransform([[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]]))


#print([[3,4,1,2,7],[9,5,3,10,8],[4,6,2,7,5],[7,9,8,1,6],[12,10,4,5,11]] == Solution().matrixRankTransform([[-37,-26,-47,-40,-13],[22,-11,-44,47,-6],[-35,8,-45,34,-31],[-16,23,-6,-43,-20],[47,38,-27,-8,43]]))

print([[7,13,1,5,4,6,9,8],[8,11,2,10,1,12,14,9],[2,14,1,11,13,7,5,3],[3,19,16,12,14,7,10,13],[8,12,6,14,5,1,4,13],[2,16,15,17,4,18,3,14],[3,7,11,6,12,13,14,10],[16,19,18,3,15,2,11,17]] == Solution().matrixRankTransform([[-23,20,-49,-30,-39,-28,-5,-14],[-19,4,-33,2,-47,28,43,-6],[-47,36,-49,6,17,-8,-21,-30],[-27,44,27,10,21,-8,3,14],[-19,12,-25,34,-27,-48,-37,14],[-47,40,23,46,-39,48,-41,18],[-27,-4,7,-10,9,36,43,2],[37,44,43,-38,29,-44,19,38]]))


print('elapse time: {} sec'.format(time.time() - stime))
