

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return None
        out = []
        for a in A:
            out.append([1 if v == 0 else 0 for v in a[::-1]])
        return out

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return None

        rows = len(A)
        cols = len(A[0])

        for y in range(rows):
            for x in range(cols//2):
                val1 = 1 if 0 == A[y][x] else 0
                val2 = 1 if 0 == A[y][cols - x - 1] else 0
                A[y][cols - x - 1], A[y][x] = val1, val2

            if cols%2 == 1:
                A[y][cols//2] = 1 if 0 == A[y][cols//2] else 0

        return A