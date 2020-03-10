

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        wnd = []
        l = r = tot = mx = 0
        
        while r < len(s):
            diff = abs(ord(s[r]) - ord(t[r]))
            wnd += diff,
            tot += diff
            
            while tot > maxCost:
                tot -= abs(ord(s[l]) - ord(t[l]))
                l += 1                
            
            mx = max(mx, r + 1 - l)
            r += 1
            
        return mx


    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        l = r = 0
        cost = 0
        mx = 0
        
        diffs = []
        for i in range(len(s)):
            diffs += abs(ord(s[i]) - ord(t[i])),
        
        while r < len(s):
            cost += diffs[r]
            
            while cost > maxCost:
                cost -= diffs[l]
                l += 1
            
            mx = max(mx, r - l + 1)
            r += 1
        
        return mx


#print(3 == SolutionEqSubStr().equalSubstring("abcd", "bcdf", 3)) 
#print(1 == SolutionEqSubStr().equalSubstring("abcd", "cdef", 3)) 
print(2 == SolutionEqSubStr().equalSubstring("abcd", "bdef", 3))
#print(2 == SolutionEqSubStr().equalSubstring("krrgw", "zjxss", 19)) 
#print(4 == SolutionEqSubStr().equalSubstring("pxezla", "loewbi", 25)) 