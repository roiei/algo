

def match(w, s):
    pos = 0
    while pos < len(s) and pos < len(w) and (w[pos] == '?' or w[pos] == s[pos]):
        pos += 1
    if pos == len(w):
        if pos == len(s):
            return True
        else:
            return False
    if w[pos] == '*':
        skip = 0
        while (pos+skip < len(s)) and (pos+1 < len(w)):
            if True == match(w[pos+1], s[pos+skip]):
                return True
            skip += 1
    return False

match_cache = []
def match_dp(w, s):
    pos = 0
    while pos < len(s) and pos < len(w) and (w[pos] == '?' or w[pos] == s[pos]):
        pos += 1
    if pos == len(w):
        if pos == len(s):
            return True
        else:
            return False
    if w[pos] == '*':
        skip = 0
        while pos+skip <= len(s):
            if True == match(w[pos+1], s[pos+skip]):
                return True
            skip += 1
    return False


wildcard_word = 't*l?*o*r?ng*s'
input_word = 'theloadoftherings'

wildcard_word = '**a'
input_word = 'aaaaaaaaaaa'


print(match(wildcard_word, input_word))
