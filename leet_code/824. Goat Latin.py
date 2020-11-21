import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []

        for i, word in enumerate(S.split()):
            oword = ''
            suffix = ''

            if set(word.lower()) | set(list('aeiou')):
                suffix = 'ma' + 'a'*(i + 1)

            if word[0].lower() not in 'aeiou':
                oword = word[1:] + word[0]
            else:
                oword = word[:]

            oword += suffix
            res += oword,

        return ' '.join(res)

stime = time.time()
print("Imaa peaksmaaa oatGmaaaa atinLmaaaaa" == Solution().toGoatLatin("I speak Goat Latin"))
#print("heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa" == Solution().toGoatLatin("The quick brown fox jumped over the lazy dog"))
#print( == Solution().toGoatLatin())
print("Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa" == Solution().toGoatLatin("Each word consists of lowercase and uppercase letters only"))
print('elapse time: {} sec'.format(time.time() - stime))

#Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa
#achEmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa


