
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def rankTeams(self, votes: [str]) -> str:
        n = len(votes[0])
        score = collections.defaultdict(int)

        for vote in votes:
            for i in range(len(vote)):
                score[vote[i]] += n - i

        freq = collections.defaultdict(list)
        #print(score)

        for k, v in score.items():
            freq[v] += k,

        freq = sorted(freq.items(), key=lambda p: p[0], reverse=True)

        res = ''
        for k, v in freq:
            res += ''.join(sorted(v))

        print(freq)
        return res


    def rankTeams(self, votes):
        count = {}
        for v in votes[0]:
            count[v] = [0] * len(votes[0]) + [v]

        print(count)

        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1
        print(count)

        res = ''

        for ch in votes[0]:
            print(count.get(ch))

        print(sorted(votes[0], key=count.get))

        return ''.join(sorted(votes[0], key=count.get))



stime = time.time()
print("ACB" == Solution().rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
# print("XWYZ" == Solution().rankTeams(["WXYZ","XYZW"]))
# print("ZMNAGUEDSJYLBOPHRQICWFXTVK" == Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
# print("ABC" == Solution().rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))
# print("M" == Solution().rankTeams(["M","M","M","M"]))
#print("VWFHSJARNPEMOXLTUKICZGYQ" == Solution().rankTeams(["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL","VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ","RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN","SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL","WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO","HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ","EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF","XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"]))
print('elapse time: {} sec'.format(time.time() - stime))