
import time


class Solution:
    def mark(self, board, rows, cols, coords, mark):
        for coord in coords:
            board[coord[0]][coord[1]] = mark

    def check(self, board, rows, cols, y, x, coords):
        if 'X' == board[y][x] or '@' == board[y][x]:
            return True
        if not (0 < y < rows-1 and 0 < x < cols-1):
            return False
        board[y][x] = '@'
        coords.append([y, x])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = [True]

        if 0 < y and board[y-1][x] == 'O':
            res.append(self.check(board, rows, cols, y-1, x, coords))
        if y < rows-1 and board[y+1][x] == 'O':
            res.append(self.check(board, rows, cols, y+1, x, coords))
        if 0 < x and board[y][x-1] == 'O':
            res.append(self.check(board, rows, cols, y, x-1, coords))
        if x < cols-1 and board[y][x+1] == 'O':
            res.append(self.check(board, rows, cols, y, x+1, coords))

        return False if False in res else True

    def solve(self, board):
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        for y in range(rows):
            for x in range(cols):
                coords = []     # must here
                if 'O' == board[y][x]:
                    if True == self.check(board, rows, cols, y, x, coords):
                        self.mark(board, rows, cols, coords, 'X')

        for y in range(rows):
            for x in range(cols):
                if board[y][x] == '@':
                    board[y][x] = 'O' 

    def solve(self, board: [[str]]) -> None:
        if not board:
            return
        rows = len(board)
        cols = len(board[0])
        def dfs(y, x):
            if board[y][x] == 'X':
                return True
            if y == 0 or y == rows - 1 or x == 0 or x == cols - 1:
                return False
            
            for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not (0 <= y + oy < rows and 0 <= x + ox < cols):
                    continue
                board[y][x] = 'X'
                if False == dfs(y + oy, x + ox):
                    board[y][x] = 'O'
                    return False
            
            print('not restored -> {}, {}'.format(y, x))
            return True
    
        for y in range(rows):
            for x in range(cols):
                if y == 0 or y == rows - 1 or x == 0 or x == cols - 1:
                    continue
                if board[y][x] == "O":
                    print('O -> {}, {}'.format(y, x))
                    dfs(y, x)

                    for b in board:
                        print(b)

board = [
['X', 'X', 'X', 'X'],
['X', 'O', 'O', 'X'],
['X', 'X', 'O', 'X'],
['X', 'O', 'X', 'X'],
]

board = [
 ["X","O","O","X","X","X","O","X","O","O"],
 ["X","O","X","X","X","X","X","X","X","X"],
 ["X","X","X","X","O","X","X","X","X","X"],
 ["X","O","X","X","X","O","X","X","X","O"],
 ["O","X","X","X","O","X","O","X","O","X"],
 ["X","X","O","X","X","O","O","X","X","X"],
 ["O","X","X","O","O","X","O","X","X","O"],
 ["O","X","X","X","X","X","O","X","X","X"],
 ["X","O","O","X","X","O","X","X","O","O"],
 ["X","X","X","O","O","X","O","X","X","O"]]


# expected
exp =  [["X","O","O","X","X","X","O","X","O","O"],
  ["X","O","X","X","X","X","X","X","X","X"],
  ["X","X","X","X","X","X","X","X","X","X"],
  ["X","X","X","X","X","X","X","X","X","O"],
  ["O","X","X","X","X","X","X","X","X","X"],
  ["X","X","X","X","X","X","X","X","X","X"],
  ["O","X","X","X","X","X","X","X","X","O"],
  ["O","X","X","X","X","X","X","X","X","X"],
  ["X","X","X","X","X","X","X","X","O","O"],
  ["X","X","X","O","O","X","O","X","X","O"]]

# output
exp = [["X","O","O","X","X","X","O","X","O","O"],
 ["X","X","X","X","X","X","X","X","X","X"],
 ["X","X","X","X","X","X","X","X","X","X"],
 ["X","X","X","X","X","X","X","X","X","O"],
 ["O","X","X","X","X","X","X","X","X","X"],
 ["X","X","X","X","X","X","X","X","X","X"],
 ["O","X","X","X","X","X","X","X","X","O"],
 ["O","X","X","X","X","X","X","X","X","X"],
 ["X","X","X","X","X","X","X","X","O","O"],
 ["X","X","X","O","O","X","O","X","X","O"]]



# board = [
# ["O","O","O","O","X","X"],
# ["O","O","O","O","O","O"],
# ["O","X","O","X","O","O"],
# ["O","X","O","O","X","O"],
# ["O","X","O","X","O","O"],
# ["O","X","O","O","O","O"]]

board = [
["O","X","X","O","X"],
["X","O","O","X","O"],
["X","O","X","O","X"],
["O","X","O","O","O"],
["X","X","O","X","O"]]

exp = [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]

stime = time.time()
sol = Solution()
sol.solve(board)

print(board == exp)

print('elapse time: {} sec'.format(time.time() - stime))

for b in board:
    print(b)