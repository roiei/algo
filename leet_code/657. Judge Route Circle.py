def judge_route_circle(seq):
    iy = ix = sy = sx = 0
    move = {
        'U' : [-1, 0],
        'D' : [1, 0],
        'L' : [0, -1],
        'R' : [0, 1]
    }
    for s in seq:
        sy += move[s][0]
        sx += move[s][1]

    if sy == iy and sx == ix:
        return True
    return False

print(judge_route_circle("UD"))
print(judge_route_circle("LL"))
