class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        substrs = []
        for i in range(len(s)):
            substr = []
            substr.append(s[i])
            for j in range(i+1, len(s)):
                if s[j] in substr:
                    break
                substr.append(s[j])
            substrs.append(substr)

        len_max = 0
        substr_max = None
        for substr in substrs:
            if len(substr) > len_max:
                len_max = len(substr)
                substr_max = substr
        return len_max

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))