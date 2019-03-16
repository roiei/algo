

def pot(a):
    global g_cnt
    g_cnt += 1
    if not a:
        return 0
    a_left_val  = a[0]  + min(pot(a[2:]), pot(a[1:-1]))
    a_right_val = a[-1] + min(pot(a[1:-1]), pot(a[:-2]))
    return max(a_left_val, a_right_val)


test_set = [[9, 8, 7, 5, 4, 6, 3, 1, 2], [1,3,4,5,1]]

g_cnt = 0
for a in test_set:
    g_cnt = 0
    print(pot(a))
    print('call cnt = ', g_cnt)