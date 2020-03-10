


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mlen = 0
        n = len(s)
        
        wnd = []
        for ch in s:
            if ch in wnd:
                while wnd and wnd[0] != ch:
                    wnd.pop(0)
                wnd.pop(0)
            wnd += ch,
            mlen = max(mlen,  len(wnd))
            
        return mlen