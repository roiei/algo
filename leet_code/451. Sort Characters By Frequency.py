
class Solution:
    def frequencySort(self, s: str) -> str:
        if not str:
            return ''
        adict = {}
        for ch in s:
            if ch not in adict:
                adict[ch] = 1
            else:
                adict[ch] += 1
        res_tuple = sorted(adict.items(), key=lambda p:p[1], reverse=True)
        return ''.join([rt[0]*rt[1] for rt in res_tuple])




sol = Solution()
ret = sol.frequencySort("tree")
print(ret)

