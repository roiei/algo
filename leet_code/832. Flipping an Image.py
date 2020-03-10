

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return None
        out = []
        for a in A:
            out.append([1 if v == 0 else 0 for v in a[::-1]])
        return out
