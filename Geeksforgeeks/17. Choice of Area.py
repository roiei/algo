


mem = {}

def choice(a, b, area, n, pre_area, depth):
    if (a, b, pre_area) in mem:
        return mem[(a, b, pre_area)]
    if a <= 0 or b <= 0:
        return 0
    depths = []
    for i in range(n):
        if i == pre_area:
            continue
        depths += 1 + choice(a + area[i][0], b + area[i][1], area, n, i, depth+1),

    mem[(a, b, pre_area)] = max(depths) if depths else depth
    return mem[(a, b, pre_area)]


area = [[3,2], [-5, -10], [-20, 5]]
print(choice(20, 20, area, len(area), -1, 0))
