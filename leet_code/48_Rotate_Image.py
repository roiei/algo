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


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

sol = Solution()
print(sol.rotate(matrix))

for y in range(len(matrix)):
    print(matrix[y])

