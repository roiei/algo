


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        l = 0
        diff = 0
        cnt = 0
        
        for ch in s:
            if ch == 'R':
                r += 1
            elif ch == 'L':
                l += 1
            
            diff = r - l
            if diff == 0:
                cnt += 1
        
        return cnt