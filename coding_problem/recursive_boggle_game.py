

board = [
['U', 'R', 'L', 'P', 'M'],
['X', 'P', 'R', 'E', 'T'],
['A', 'I', 'A', 'E', 'T'],
['X', 'T', 'N', 'Z', 'Y'],
['X', 'O', 'Q', 'R', 'S']
]

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def in_range(y, x):
    if 0 <= y <= 4 and 0 <= x <= 4:
        return True
    return False

def has_word(y, x, word):
    if in_range(y, x) == False:
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    for dir in range(8):
        next_y = y + dy[dir]
        next_x = x + dx[dir]
        if has_word(next_y, next_x, word[1:]) == True:
            return True
    return False

print(has_word(1, 1, 'PRETTY'))