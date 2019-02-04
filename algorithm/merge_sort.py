


def merge(a, b, c, offa, na, offb, nb, offc):
    i = j = k = 0
    while k < na + nb:
        if j < nb and i < na:
            if a[offa + i] > b[offb + j]:
                c[offc + k] = b[offb + j]; k += 1; j += 1
            else:
                c[offc + k] = a[offa + i]; k += 1; i += 1
        else:
            if j >= nb:
                c[offc + k] = a[offa + i]; k += 1; i += 1
            else:
                c[offc + k] = b[offb + j]; k += 1; j += 1

def sort_merge_my(a, n):
    b = [0 for i in range(n)]
    unit   = 1
    first  = 0
    second = unit
    while unit < n:
        while second + unit <= n:
            i = k = first
            j = second
            merge(a, a, b, first, unit, second, unit, first)
            first  += 2*unit
            second += 2*unit
        a[:first] = b[:first]   # do not overrun with zeros..
        unit  *= 2
        first  = 0
        second = unit

    #     a, b, c, offa,  na,      offb,    nb,          offc
    merge(a, a, b, first, unit//2, unit//2, n - unit//2, first)
    a[:n] = b[:n]

a = [7, 11, 5, 1, 9, 3]
sort_merge_my(a, len(a))
print(a)