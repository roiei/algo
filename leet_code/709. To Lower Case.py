class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ''
        for ch in str:
            if 'A' <= ch <= 'Z':
                res += chr(ord(ch)-ord('A')+ord('a'))
            else:
                res += ch
        return res