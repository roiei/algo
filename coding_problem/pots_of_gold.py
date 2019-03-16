

def maximize(pots):
    if not pots:
        return 0

    choose_leftmost   = pots[0]
    next_choose_left  = maximize(pots[2:])
    next_choose_right = maximize(pots[1:-1])
    next_value = min(next_choose_left, next_choose_right)

    print('lm = {}, nx = {}'.format(choose_leftmost, next_value))

    left_case = choose_leftmost + next_value

    choose_rightmost  = pots[-1]
    next_choose_left  = maximize(pots[1:-1])
    next_choose_right = maximize(pots[0:-2])
    next_value = min(next_choose_left, next_choose_right)

    print('rm = {}, nx = {}'.format(choose_rightmost, next_value))

    right_case = choose_rightmost + next_value

    return max(left_case, right_case)


print(maximize([9,8,7,5,4,6,3,1,2]))
print(maximize([1,3,4,5,1]))

