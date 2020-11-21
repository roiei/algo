    valley_cnt = 0
    sea_level = 0   # 0: even, 1: over, -1: under
    level = 0
    start_valley = False
    for step in s:        
        if 'U' == step:
            level += 1
        elif 'D' == step:
            level -= 1
        if level < sea_level:
            start_valley = True
        if level >= sea_level:
            if True == start_valley:
                valley_cnt += 1
                start_valley = False
        print('step = {}, level = {}, cnt = {}'.format(step, level, valley_cnt))
    return valley_cnt