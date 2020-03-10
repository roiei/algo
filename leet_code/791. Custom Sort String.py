import time


class Solution:
    def customSortString1(self, S: str, T: str) -> str:
        n = len(T)
        output = ''
        for i in range(len(S)):
            for j in range(len(T)):
                if T[j] == S[i]:
                    output += T[j]
        print(output)
        subfix = [v for v in T if v not in S]
        for i in range(len(subfix)):
            output += subfix[i]
        return output

    def customSortString(self, S: str, T: str) -> str:
        n = len(T)
        common = []
        for ch_s in S:
            for ch_t in T:
                if ch_s == ch_t:
                    common.append(ch_s)
        not_common = [ch for ch in T if ch not in S]
        return ''.join(common + not_common)


graph = [[1,2], [3], [3], []]  # [[0,1,3],[0,2,3]] 

stime = time.time()
sol = Solution()
#ret = sol.customSortString('cba', 'abcd')
ret = sol.customSortString("cbafg", "abcd") #"cbad"
#ret = sol.customSortString("kqep", "pekeq") #"kqeep"

print('elapse time: {} sec'.format(time.time() - stime))
print(ret)