class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]

    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s) - 1
        
        while l < len(s)//2:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1