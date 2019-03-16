class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> None:
        height = len(board)
        width = len(board[0])
        next_board = [[0 for i in range(width)] for j in range(height)]
        for i in range(height):
            for j in range(width):
                next_board[i][j] = board[i][j]

        for y in range(height):
            for x in range(width):
                cnt_live = 0
                cnt_dead = 0
                if y > 0 and x > 0:
                    if 1 == board[y-1][x-1]:
                        cnt_live += 1
                    else:
                        cnt_dead += 1
                if y > 0:
                    if 1 == board[y-1][x]:
                        cnt_live += 1
                    else:
                        cnt_dead += 1
                if y > 0 and x < width-1:
                    if 1 == board[y-1][x+1]:
                        cnt_live += 1
                    else:
                        cnt_dead += 1
                if x < width-1:
                    if 1 == board[y][x+1]:
                        cnt_live += 1
                    else:
                        cnt_dead += 1
                if y < height-1 and x < width-1:
                    if 1 == board[y+1][x+1]:
                        cnt_live += 1
                    else:
                        cnt_dead += 1
                if y < height-1:
                    if 1 == board[y+1][x]:
                        cnt_live += 1
                    else:
                        cnt_dead += 1
                if y < height-1 and x > 0:
                    if 1 == board[y+1][x-1]:
                        cnt_live += 1
                    else:
                        cnt_dead += 1
                if x > 0:
                    if 1 == board[y][x-1]:
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
            for j in range(width):
                board[i][j] = next_board[i][j]

in_game = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

sol = Solution()
ret = sol.gameOfLife(in_game)
print(ret)

