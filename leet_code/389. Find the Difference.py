class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not t:
            return ''
        ls = list(s)
        lt = list(t)
        for i in range(len(lt)):
            if lt[i] in ls:
                ls.remove(lt[i])
                lt[i] = '-'
        return ''.join([ch for ch in lt if ch != '-'])