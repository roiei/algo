N, K = 20, 1
pos = list('HHPHPPHHPPHPPPHPHPHP')

# N, K = 20, 2
# pos = 'HHHHHPPPPPHPHPHPHHHP'


cnt = 0
hpos = 0
i = 0


while i < N:
    while i < N and 'P' != pos[i]:
        i += 1
 
    for j in range(max(0, hpos, i - K), min(i + K + 1, N)):
        if pos[j] == 'H':
            cnt += 1
            pos[j] = '.'
            hpos = j + 1
            break

    i += 1


print(cnt)
