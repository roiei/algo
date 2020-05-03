
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:

    # timeout
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        wnd = 'croak'
        s = list(croakOfFrogs)
        cnt = 0

        while True:
            pre_len = len(s)
            i = 0
            j = 0
            idxs = []
            rm_idxs = []

            while i < len(s):
                if s[i] == wnd[j]:
                    idxs += i,
                    j += 1
                    if j == len(wnd):
                        rm_idxs += idxs
                        idxs = []
                        j = 0
                i += 1

            if not rm_idxs:
                if s:
                    return -1
                break

            while s and rm_idxs:
                s.pop(rm_idxs.pop()) 

            cnt += 1

        return cnt

    def minNumberOfFrogs(self, croakOfFrogs):
        seq = "croak"
        freq = collections.defaultdict(int)
        for ch in seq:
            freq[ch] = 0

        res = 0
        dep = {'c':None, 'r':'c', 'o':'r', 'a':'o', 'k':'a'}
        
        for ch in croakOfFrogs:
            if ch not in freq:
                return -1
            
            freq[ch] += 1

            if dep[ch] and freq[dep[ch]] < freq[ch]:
                return -1

            if ch == 'k':
                for k in seq:
                    freq[k] -= 1

            res = max(res, freq[ch])

        if len(freq.values()) != list(freq.values()).count(0):
            return -1
                    
        return res

        
        
stime = time.time()
print(1 == Solution().minNumberOfFrogs("croakcroak"))
print(2 == Solution().minNumberOfFrogs("crcoakroak"))
print(-1 == Solution().minNumberOfFrogs("croakcrook"))
print(2 == Solution().minNumberOfFrogs("crocakcroraoakk"))
print(-1 == Solution().minNumberOfFrogs("croakcroa"))
print(229 == Solution().minNumberOfFrogs("ccccccccccrrccccccrcccccccccccrcccccccccrcccccccccccrcccccrcccrrcccccccccccccrocrrcccccccccrccrocccccrccccrrcccccccrrrcrrcrccrcoccroccrccccccccorocrocccrrrrcrccrcrcrcrccrcroccccrccccroorcacrkcccrrroacccrrrraocccrrcrrccorooccrocacckcrcrrrrrrkrrccrcoacrcorcrooccacorcrccccoocroacroraoaarcoorrcrcccccocrrcoccarrorccccrcraoocrrrcoaoroccooccororrrccrcrocrrcorooocorarccoccocrrrocaccrooaaarrcrarooaarrarrororrcrcckracaccorarorocacrrarorrraoacrcokcarcoccoorcrrkaocorcrcrcrooorrcrroorkkaaarkraroraraarooccrkcrcraocooaoocraoorrrccoaraocoorrcokrararrkaakaooroorcororcaorckrrooooakcarokokcoarcccroaakkrrororacrkraooacrkaraoacaraorrorrakaokrokraccaockrookrokoororoooorroaoaokccraoraraokakrookkroakkaookkooraaocakrkokoraoarrakakkakaroaaocakkarkoocokokkrcorkkoorrkraoorkokkarkakokkkracocoaaaaakaraaooraokarrakkorokkoakokakakkcracarcaoaaoaoorcaakkraooaoakkrrroaoaoaarkkarkarkrooaookkroaaarkooakarakkooaokkoorkroaaaokoarkorraoraorcokokaakkaakrkaaokaaaroarkokokkokkkoakaaookkcakkrakooaooroaaaaooaooorkakrkkakkkkaokkooaakorkaroaorkkokaakaaaaaocrrkakrooaaroroakrakrkrakaoaaakokkaaoakrkkoakocaookkakooorkakoaaaaakkokakkorakaaaaoaarkokorkakokakckckookkraooaakokrrakkrkookkaaoakaaaokkaokkaaoakarkakaakkakorkaakkakkkakaaoaakkkaoaokkkakkkoaroookakaokaakkkkkkakoaooakcokkkrrokkkkaoakckakokkocaokaakakaaakakaakakkkkrakoaokkaakkkkkokkkkkkkkrkakkokkroaakkakaoakkoakkkkkkakakakkkaakkkkakkkrkoak"))
print('elapse time: {} sec'.format(time.time() - stime))