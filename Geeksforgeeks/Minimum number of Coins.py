

def min_coin(val, coins):
    if val == 0:
        return 0
    cnt = 0
    for i in range(len(coins)):
        if val < coins[i]:
            break
        cnt += 1
    if cnt > len(coins)-1:
        cnt = len(coins)-1
    res = []
    while val > 0:
        while cnt > 0 and val < coins[cnt]:
            cnt -= 1
        val -= coins[cnt]
        res += coins[cnt],
    return res


coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
#print(min_coin(43, coins))
print(min_coin(8098, coins))

for t in range(tc):
    val = int(input())
    res = min_coin(val, coins)
    for r in res:
        print(r, end=' ')
    print()
