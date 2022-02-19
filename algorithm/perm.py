import collections


def permutate2(r, space, stk, perms):
    while stk and r:
        nstk = []

        while stk:
            cur = stk.pop()

            for i in range(len(space)):
                nstk += cur + space[i],

        stk = nstk
        r -= 1

    for item in stk:
        perms.append(item)


def permutate(r, space, perm, perms):
    if len(perm) == r:
        perms.append(perm)
        return

    for i in range(len(space)):
        if space[i] in perm:
            continue
        permutate(r, space, perm + space[i], perms)


def call_perm():
    perms1 = []
    permutate(2, ['R', 'G', 'B'], '', perms1)
    print(len(perms1), perms1)

    perms2 = []
    permutate2(1, ['R', 'G', 'B'], ['R', 'G', 'B'], perms2)
    print(len(perms2), perms2)

    print(perms1 == perms2)

call_perm()


def combinate(r, start, space, seq, res):
    if len(seq) == r:
        res.append(seq)
        return

    for i in range(start, len(space)):
        combinate(r, i + 1, space, seq + space[i], res)


# res = []
# combinate(2, 0, ['R', 'G', 'B'], '', res)
# print(res)






