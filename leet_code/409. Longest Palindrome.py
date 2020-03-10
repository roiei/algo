import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def longestPalindrome(self, s):
        length = 0
        elems = collections.Counter(s)
        uniq = set(s)
        for uletter in uniq:            
            v = elems[uletter]
            even = v if 0 == v%2 else (v//2)*2
            left = v - even
            length += even
            if 0 == length%2:
                length += left
        return length


# print(collections.Counter([1, 2, 3, 4, 5, 6, 7, 3, 5, 7, 7]))
# print(collections.Counter('This is excellent Python package collections'))
# print(collections.Counter('this is Python and this Python is powerful'.split()))



stime = time.time()
#print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
print(7 == Solution().longestPalindrome("abccccdd"))
print('elapse time: {} sec'.format(time.time() - stime))
