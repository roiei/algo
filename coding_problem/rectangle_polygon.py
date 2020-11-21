pol = [-2,3,2,-2,-3,-4,-7,-5]
out_pol = [4,3,-2,-2,3,2,5,7]

rvs_pol = []
pol.append(pol[0])
for i in range(len(pol)-1):
    if 0 > pol[i]:
        if pol[i+1] < 0:
            rvs_pol.append(-1*pol[i+1])
        else:
            rvs_pol.append(pol[i+1])
    else:
        if pol[i+1] < 0:
            rvs_pol.append(pol[i+1])
        else:
            rvs_pol.append(-1*pol[i+1])

rvs_pol = rvs_pol[::-1]
rvs_pol.extend(rvs_pol)
print(len(rvs_pol))
print(len(out_pol))

for i in range(len(out_pol)):
    cnt = 0
    for j in range(len(out_pol)):
        if rvs_pol[i+j] == out_pol[j]:
            cnt += 1
    if cnt == len(out_pol):
        print('1')
