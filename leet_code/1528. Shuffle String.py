

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        loc = collections.defaultdict(str)
        for idx, ch in zip(indices, list(s)):
            loc[idx] = ch
        
        loc = sorted(loc.items(), key=lambda p: p[0])
        res = ''
        for idx, ch in loc:
            res += ch
        return res

