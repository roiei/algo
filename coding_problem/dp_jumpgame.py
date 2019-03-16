


jump_game_in1 = [
[2, 5, 1, 6, 1, 4, 1],
[6, 1, 1, 2, 2, 9, 3],
[7, 2, 3, 2, 1, 3, 1],
[1, 1, 3, 1, 7, 1, 2],
[4, 1, 2, 3, 4, 1, 2],
[3, 3, 1, 2, 3, 4, 1],
[1, 5, 2, 9, 4, 7, 0],
]

# jump_game_in1 = [
# [2, 5, 1, 6, 1, 4, 1],
# [6, 1, 1, 2, 2, 9, 3],
# [7, 2, 3, 2, 1, 3, 1],
# [1, 1, 3, 1, 7, 1, 2],
# [4, 1, 2, 3, 4, 1, 3],
# [3, 3, 1, 2, 3, 4, 1],
# [1, 5, 2, 9, 4, 7, 0],
# ]

# 0 is end

g_recur_cnt = 0
def do_dump_game(board, size, y, x):
    global g_recur_cnt
    g_recur_cnt += 1
    if x == size-1 and y == size-1:
        return True
    if x >= size or y >= size:
        return False
    move_size = board[y][x]
    return do_dump_game(board, size, move_size + y, x) or \
        do_dump_game(board, size, y, move_size + x)


g_dp_cnt = 0
def do_dump_game_dp(cache, board, size, y, x):
    global g_dp_cnt
    g_dp_cnt += 1
    if x == size-1 and y == size-1:
        return True
    if x >= size or y >= size:
        return False
    if -1 != cache[y][x]:
        return cache[y][x]
    move_size = board[y][x]
    cache[y][x] = do_dump_game_dp(cache, board, size, move_size + y, x) or \
        do_dump_game_dp(cache, board, size, y, move_size + x)
    return cache[y][x]

dump_game_cache = [[-1 for i in range(len(jump_game_in1[0]))] for j in range(len(jump_game_in1[0]))]

print(do_dump_game(jump_game_in1, len(jump_game_in1[0]), 0, 0))
print(g_recur_cnt)
print(do_dump_game_dp(dump_game_cache, jump_game_in1, len(jump_game_in1[0]), 0, 0))
print(g_dp_cnt)






