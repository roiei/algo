import time


class Solution:
    def findReplaceString(self, S: str, indexes: [int], sources: [str], targets: [str]) -> str:
        if '' == S:
            return ''
        
        out = list(S)
        infos = []

        # indexes : 3, 5, 1
        # sources : kg, ggq, mo
        # targets : s, so, bfr

        # (3, kg, s), (5, ggq, so), (1, mo, bfr)
        for i in range(len(indexes)):
            infos += (indexes[i], sources[i], targets[i]),

        # (5, ggq, so), (3, kg, s), (1, mo, bfr)
        infos.sort(key=lambda p:p[0], reverse=True)

        pre = 0
        n = len(S)
        for i in range(len(infos)):
            if infos[i][0] + len(infos[i][1]) > n:
                continue
            start = infos[i][0]
            end = start + len(infos[i][1])

            if S[start:end] == infos[i][1]:
                out[start:end] = infos[i][2]

        return ''.join(out)

    def findReplaceString(self, S: str, indexes: [int], sources: [str], targets: [str]):
        s = list(S)
        for idx, src, tgt in sorted(list(zip(indexes, sources, targets)), key=lambda p: p[0], reverse=True):
            if ''.join(s[idx:idx + len(src)]) != src:
                continue

            s[idx:idx + len(src)] = list(tgt)

        return ''.join(s)

    def findReplaceString(self, S: str, indexes: [int], sources: [str], targets: [str]):
        s = list(S)

        params = sorted(zip(indexes, sources, targets), key=lambda p: p[0], reverse=True)
        for idx, src, tgt in params:
            if ''.join(s[idx:idx + len(src)]) != src:
                continue

            s[idx:idx + len(src)] = list(tgt)

        return ''.join(s)

        



stime = time.time()
print('eeebffff' == Solution().findReplaceString('abcd', [0,2], ['a', 'cd'], ['eee', 'ffff']))
print("eeecd" == Solution().findReplaceString('abcd', [0,2], ["ab","ec"], ["eee","ffff"])) # 
print("vbfrssozp" == Solution().findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"])) # 
print('elapse time: {} sec'.format(time.time() - stime))
