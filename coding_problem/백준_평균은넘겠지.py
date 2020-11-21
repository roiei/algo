tc = int(input())
for i in range(tc):
    cnum = list(map(int, input().split()))
    n = cnum[0]
    cnum = cnum[1:]
    avg = sum(cnum)/n
    cnt = 0
    for i in cnum:
        if i > avg:
            cnt+= 1
    print('{:.3f}%'.format((cnt/n)*100))
    