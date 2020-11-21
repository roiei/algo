  

def compute_lps(pat, n, lps):
    length = 0;
    i = 1

    while (i < n):
        if (pat[i] == pat[length]):
            length += 1
            lps[i] = length
            i += 1
        else:
            if (length != 0):
                length = lps[length - 1]; 
            else:
                lps[i] = 0
                i += 1


def kmp_search(txt, pat):
    m = len(txt)
    n = len(pat)

    lps = [0]*n

    res = []
    compute_lps(pat, n, lps)

    i = j = 0

    while i < m:
        if txt[i] == pat[j]:
            i += 1
            j += 1

        if j == n:
            res += i - j,
            j = lps[j - 1]
        elif i < m and txt[i] != pat[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return res



#print(10 == kmp_search("ABABDABACDABABCABAB", "ABABCABAB"))
print([2, 7] == kmp_search("kkabbzpabbq", "abb"))
