class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        if 1 == len(s):
            return 0
        min_idx = 0x7FFFFFFF
        skip = []
        for i in range(len(s)):
            if s[i] in skip:
                continue                
            repeat = False
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    repeat = True
                    break
            if repeat == False:
                if min_idx > i:
                    min_idx = i
            else:
                skip.append(s[i])
        return min_idx if min_idx != 0x7FFFFFFF else -1  
