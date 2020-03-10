import copy

class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> None:
        height = len(board)
        width = len(board[0])
        dirs = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        next_board = [[0 for i in range(width)] for j in range(height)]
        next_board = copy.deepcopy(board)

        for y in range(height):
            for x in range(width):
                cnt_live = 0
                cnt_dead = 0
                for dir in dirs:
                    ny = y + dir[0]
                    nx = x + dir[1]
                    if 0 <= ny < height and 0 <= nx < width:
                        if 1 == board[ny][nx]:
                            cnt_live += 1
                        else:
                            cnt_dead += 1
                if 0 == board[y][x]:
                    if 3 == cnt_live:
                        next_board[y][x] = 1
                else:
                    if cnt_live < 2 or cnt_live > 3:
                        next_board[y][x] = 0

        for i in range(height):
            board[i] = next_board[i][:]  # in-place !!!

in_game = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

sol = Solution()
ret = sol.gameOfLife(in_game)
print(ret)

