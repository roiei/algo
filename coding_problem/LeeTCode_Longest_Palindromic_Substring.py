
# https://leetcode.com/problems/longest-palindromic-substring/
# Level: Medium


def lps(s):
    if s in cache:
        return cache[s][0], cache[s][1]
    if len(s) == 1:
        return True, s[0]
    
    if s == s[::-1]:
        return True, s
    
    is_palin1, palin1 = lps(s[1:])
    is_palin2, palin2 = lps(s[:-1])
    
    len_p1 = len_p2 = 0
    if is_palin1 == True:
        len_p1 = len(palin1)
    if is_palin2 == True:
        len_p2 = len(palin2)
    
    res_palin = None
    if len_p1 > len_p2:
        res_palin = palin1
    else:
        res_palin = palin2

    cache[s] = []
    cache[s].append(True if is_palin1 == True or is_palin2 == True else False)
    cache[s].append(res_palin)
    return cache[s]

def longestPalindrome_stack(s: str) -> str:
    if len(s) == 1:
        return s
    if s == s[::-1]:
        return s

    res = []
    res_len = []
    stk = []
    stk.append(s[1:])
    stk.append(s[:-1])
    cache.clear()

    while True:
        nstk = []
        res_is_palin = [False for i in range(2)]
        res_string   = [False for i in range(2)]
        idx = 0
        while stk:
            s = stk.pop()
            if s in cache:
                continue
            if len(s) <= 1:
                print('len 1 ', s)
                res.append(s)
                res_len.append(len(s))
                continue
            if s == s[::-1]:
                print('palin: ', s)
                res.append(s)
                res_len.append(len(s))
                continue
            nstk.append(s[1:])
            nstk.append(s[:-1])
            idx += 1
            cache[s] = s[:]

        stk = nstk
        if not stk:
            break

    if res_len:
        return res[res_len.index(max(res_len))]
    return ''

def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    
    is_palin, palin = lps(s)
    return palin


instr = 'babad'
#instr = "kyyrjtdplseovzwjkykrjwhxquwxsfsorjiumvxjhjmgeueafubtonhlerrgsgohfosqssmizcuqryqomsipovhhodpfyudtusjhonlqabhxfahfcjqxyckycstcqwxvicwkjeuboerkmjshfgiglceycmycadpnvoeaurqatesivajoqdilynbcihnidbizwkuaoegmytopzdmvvoewvhebqzskseeubnretjgnmyjwwgcooytfojeuzcuyhsznbcaiqpwcyusyyywqmmvqzvvceylnuwcbxybhqpvjumzomnabrjgcfaabqmiotlfojnyuolostmtacbwmwlqdfkbfikusuqtupdwdrjwqmuudbcvtpieiwteqbeyfyqejglmxofdjksqmzeugwvuniaxdrunyunnqpbnfbgqemvamaxuhjbyzqmhalrprhnindrkbopwbwsjeqrmyqipnqvjqzpjalqyfvaavyhytetllzupxjwozdfpmjhjlrnitnjgapzrakcqahaqetwllaaiadalmxgvpawqpgecojxfvcgxsbrldktufdrogkogbltcezflyctklpqrjymqzyzmtlssnavzcquytcskcnjzzrytsvawkavzboncxlhqfiofuohehaygxidxsofhmhzygklliovnwqbwwiiyarxtoihvjkdrzqsnmhdtdlpckuayhtfyirnhkrhbrwkdymjrjklonyggqnxhfvtkqxoicakzsxmgczpwhpkzcntkcwhkdkxvfnjbvjjoumczjyvdgkfukfuldolqnauvoyhoheoqvpwoisniv"
#instr = "eabcb"
instr = "ac"
instr = "eabcb"
cache = {}
print(longestPalindrome_stack(instr))
#print(longestPalindrome_stack('a'))