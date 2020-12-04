class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        width = len(matrix[0])
        rotated = [[0 for x in range(width)] for y in range(height)]

        for y in range(height):
            for x in range(width):
                rotated[x][height-1-y] = matrix[y][x]
        for y in range(height):
            for x in range(width):
                matrix[y][x] = rotated[y][x]
        return None

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for y in range(rows):
            for x in range(y, cols):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

        for y in range(len(matrix)):
            print(matrix[y])

        for y in range(rows):
            matrix[y].reverse()


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

sol = Solution()
print(sol.rotate(matrix))

for y in range(len(matrix)):
    print(matrix[y])

