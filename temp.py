    

from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        diags = []
        for dia in range(rows + cols - 1):
            diags += [],

        for y in range(rows):
            for x in range(cols):
                diags[y + x] += matrix[y][x],

        toggle = True
        res = []
        for diag in diags:
            if toggle:
                diag.reverse()

            toggle = not toggle
            res += diag


        return res


print([1,2,4,7,5,3,6,8,9] == Solution().findDiagonalOrder([
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]))

