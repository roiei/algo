
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        l = 0
        r = len(s) - 1
        mx = 0
        freq = collections.Counter([ch for ch in s if ch in 'aeiou'])

        def dfs(l, r, freq, mx):
            if r - l + 1 <= mx[0]:
                return 0
            
            if (l, r) in mem:
                return mem[(l, r)]

            if l > r:
                return 0
            
            ret = 0

            if not any(map(lambda p: p%2, freq.values())):
                ret = mx[0] = max(r - l + 1, mx[0])
                mem[(l, r)] = ret
                return ret

            offset = 0
            if s[l] in 'aeiou' and freq[s[l]] > 0:
                offset = 1
            freq[s[l]] -= offset
            ret = max(ret, dfs(l + 1, r, freq, mx))
            freq[s[l]] += offset

            offset = 0
            if s[r] in 'aeiou' and freq[s[r]] > 0:
                offset = 1
            freq[s[r]] -= offset
            ret = max(ret, dfs(l, r - 1, freq, mx))
            freq[s[r]] += offset

            mem[(l, r)] = ret
            return ret

        mx = [0]
        mem = {}
        ret = dfs(0, r, freq, mx)
        return mx[0]


    def findTheLongestSubstring(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        mx = 0
        freq = collections.Counter([ch for ch in s if ch in 'aeiou'])

        def dfs(l, r, freq, mx):
            if r - l + 1 <= mx[0]:
                return 0
            
            if (l, r) in mem:
                return mem[(l, r)]

            if l > r:
                return 0
            
            ret = 0

            if not any(map(lambda p: p%2, freq.values())):
                ret = mx[0] = max(r - l + 1, mx[0])
                mem[(l, r)] = ret
                return ret
            
            for idx, lo, ro in [(l, 1, 0), (r, 0, 1)]:
                offset = 0
                if s[idx] in 'aeiou' and freq[s[idx]] > 0:
                    offset = 1
                freq[s[idx]] -= offset
                ret = max(ret, dfs(l + lo, r - ro, freq, mx))
                freq[s[idx]] += offset
                
            mem[(l, r)] = ret
            return ret

        mx = [0]
        mem = {}
        ret = dfs(0, r, freq, mx)
        return mx[0]
           

            
stime = time.time()
# print(13 == Solution().findTheLongestSubstring("eleetminicoworoep"))
# print(5 == Solution().findTheLongestSubstring("leetcodeisgreat"))
# print(6 == Solution().findTheLongestSubstring("bcbcbc"))
print(Solution().findTheLongestSubstring("lcwbgnkxnooovtxtuuolbgvieqyxdzyngkdaxuhgwzmgjjvylhavhtijfzvwdalxewsympoyvdhtlbchfgnexmmslcbrozsljwlxzkladmjibvyqpibpkwnxosrqhfqbmigkgxdtfnnsitxecihwisfonaejqeenboqxpqxbmdwzxjnodurnznaitbjikqaerbgkxdfjxnqyecqpqcnluezomtkvjprcqeaucgttwlpqeyfwenybcluxwzjvixlljnmpolktwnezewpiuwinsptbjqzplpeoeuwpehkycvrsslfznunjihtauplcipxmobnipqekegxmddzkepuqzoqepebgwmkuxipjbncgaskmzjhjnlokvxidvlbjgxsdtxiaikdmojrilepbdmokaouhekegpfjlhuywvgtbtozivvooplnnchlbkdvmrwwpkegczippokorcptixrudwszencxemdnxrgearvtddcukdvsrulnvmcnuojxynomtrteotpmdkiueivbdyfxvbakkbfnotanrsmdvmbaehqpumkejtessereyeshxgagprozlpunqanhwmitayqkdzqyhnieqosyrlidxxxcwlmolnvqopmrabpkyhdalcwfwpdheoxcfuiypwlfhbjuorrotjhajpeggfjcifmuzyszjxyfomvczltlhazrtfotejmekkiaegiguabubojhqyudxctegfanffokbotqlwjsertqbhdophqkdvjeiunidaalqfbkfbbaihaxjpxxtupkscgflwxczlelgomoltschhdhcxjqlcdstlhrjyujzdfwngoeygcncmeshjitqxspmddvlopvmgskeuikugtbvmikzdueglpuksbbwoeopqygziitejdkhkkgydngnyeqrcmamemltyqmtexvcyvqhygppmywkiraqyqwxxiamxqmeftidndwpmbpcschkmtvvklwvyihneyhvmtxbhgseskfdygnbqkrywllvwnhlymchoelulcoqznmyicooveiwwazqlnhlwozkoqyaezwyhzwdhilhsfollwbwvfmrllvrsnjqiocbdrixjzgnrszghicnmvqjjtpcnhwgpdqlsyrcbckhocgboecvpczbepewpnpjatirudtcurrtlbhrvreaymbekvmrzctyojkgnpcmyizauvudjxhssmamcuschcnqorjqybepptlerdgirzapuvsoeekmoitoszlwmyvtscagrhhtvlnrydcayhukhxgqfrcqfbjuiswvklnlygatspefmafailygnvgzhnvsgnsmbfsaugdbjermtlfsyvffqepucofzyjilohswbxhugzzihzxwnxwiwhlzpnzgoqvqzkbhhrendrcynnqmtodzgbmgrwgnqxqwtqtpyludmuvyjqzlkfnvzrhgchcivnxhpuibmlmongbjheekvvxrvjtsonvjlxkihomxkbsygzyvdvuehlewqoymiankekcgmgmtqrcvuogdezmdmyqsxzyhoyprcfyalbsoeypmgxgtbkgpixfrpqxqnbegajnwcfuamjqejefjqhzzvjzotgqgwbgtmklvmybvmcfpeljfbwpollltqxrgyrehnzvchijrokuoapwpeanmfjrwmgsvmzxwahupklojcbqkfeblphtuwbbapooynhmfdhjjhadgnvjpyizjduoeikzjsrkbjgioqxqhyakodcnlibewwuqjlzkmfybokfthpftnrmdjyctofsnpuexcarwrpstrehbrzjnzvsoislrkqlsbfnhpulvixxyhctijqybjppwfcvsqrgbssqkjcrthsufevxnutkuwgtyovfaygbacmzlngfanbhbmdllrtemqudxkpuaohmrcntsmalqjhmpmlbbntnsfwekgepnkyyalllxczymewubebxjikbceehkgyfognlejzsfoasfxudbxenvjqygbctqyqrwnxiwprooustcskdjhybhdgfuymymueshrugpwsuevxuydmolvatzpupybhtjfqtpcxkciwzqjverubkceqwefvyatrabcyrlpbvquvrcoosvailoclcffysasmgsvhepdlqvptdxtrvfqjdjctdskrosxsjojyqozzrosejsicvjbsmwepsuyxwkvidsjnhhmrscmveibviyhkcimdehpkonycqsobngmssvyittyeembauboalqokzfwvgxotgvgmkywoiifjvcyttrcqtpssrhdpdoqrfdwukqwzmshqdzohdycpisqjaktzvzmhneqsocpinxzrsrcwdmdimbcrlcmvppxvuufmbimvmmoawvhrecpmgdywwogmumnaziaybpxneytfxgqmjcrbnweofjbujsjbtqkjbpcfxuyvytmwupiozanbjyblgkfhecbdejkpsstpamsrmhxqerydnrmhratsrknzmruvgenfdsdxjflppyqfsiuwhicwqkhuztrhiyfuebolethjxbnopxbfrmzvvpuxkjiflvqxxlcynhwldlhwclvrvvvjbslqamvdaasfodglcqemfotdqiwpzflveduecumffhzjdbtgatwgazuowgtmjekltmdzttgkanoxgfaqiohzccgtxehzhwrlqqasqgobdfnevzpqhhblfzrvfnrhilyyuztrgjshdrbkjrfxenkrjtayurhakpbgmdowuzmprrgyyodvugyyufuitwiaczvvmazgqkiusgypreobmqmmbubjlhxgorppbyrgdkwjnxzhwxfisivrsldvwlnqnophdfqtotobdcmmyiguvpsvvltmrqzdsahpmiticfmdzb"))
print('elapse time: {} sec'.format(time.time() - stime))