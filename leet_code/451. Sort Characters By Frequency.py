
class Solution(object):
    def frequencySort(self, s):
        adict = {}
        for i in range(len(s)):
            if s[i] not in adict:
                adict[s[i]] = 1
            else:
                adict[s[i]]+= 1

        adict = sorted(adict.items(), key=lambda param : param[1], reverse=True)
        output = ''
        for i in range(len(adict)):
            output += adict[i][0]*adict[i][1]
        return output


sol = Solution()
ret = sol.frequencySort("tree")
print(ret)

