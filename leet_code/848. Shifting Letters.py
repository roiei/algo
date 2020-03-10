class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        n = len(shifts)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]

        out = []
        for i in range(n):
            idx = ((ord(S[i]) - ord('a')) + shifts[i])%26
            out += chr(idx + ord('a')),
        return ''.join(out)
