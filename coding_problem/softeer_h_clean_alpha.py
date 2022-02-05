

P, N = 3, 3
virus = [1, 2, 3]
mul = 3


if len(virus) >= 2:
    for i in range(len(virus) - 2, -1, -1):
        virus[i] = (virus[i]*mul)%1000000007
        mul = (mul*P)%1000000007

print(sum(virus)%1000000007)