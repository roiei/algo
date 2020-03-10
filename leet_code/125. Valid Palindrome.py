import time
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = ''
        s = s.lower()
        s = "".join(re.findall("[a-zA-Z0-9]+", s)) 
        return True if s == s[::-1] else False


stime = time.time()
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
#print(Solution().isPalindrome('0P'))


print('elapse time: {} sec'.format(time.time() - stime))



