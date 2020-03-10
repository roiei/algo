import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def check_exist(self, mergeds, new_email):
        for i in range(len(mergeds)):
            for item in mergeds[i]:
                if item == new_email:
                    return i
        return -1

    def merge(self, merge, account):
        for i in range(1, len(account)):
            if account[i] not in merge:
                merge.append(account[i])

    def sort(self, merged):
        for i in range(len(merged)):
            merged[i][1:] = sorted(merged[i][1:])

        for i in range(len(merged)):
            for j in range(i+1, len(merged)):
                if merged[i][0] > merged[j][0]:
                    merged[i], merged[j] = merged[j], merged[i]

    def remove_duplicate(self, merged):
        for i in range(len(merged)):
            new_row = merged[i][::]

            # 1. count
            cnts = {}
            for j in range(len(merged[i])):
                if merged[i][j] not in cnts:
                    cnts[merged[i][j]] = merged[i].count(merged[i][j])

            # 2. remove
            for k,v in cnts.items():
                if v > 1:
                    for l in range(v-1):
                        merged[i].remove(k)

    def accountsMerge(self, accounts: 'List[List[str]]') -> 'List[List[str]]':
        while True:
            mergeds = []
            merge_cnt = 0
            for account in accounts:
                merge_idx = -1
                for idx_email in range(1, len(account)):
                    merge_idx = self.check_exist(mergeds, account[idx_email])
                    if -1 != merge_idx:
                        break
                if -1 != merge_idx:
                    self.merge(mergeds[merge_idx], account)
                    merge_cnt += 1
                else:
                    mergeds.append(account[::])
            if 0 == merge_cnt:
                break
            accounts = mergeds

        self.remove_duplicate(mergeds)
        self.sort(mergeds)
        return mergeds


    def accountsMerge(self, accounts: [[str]]) -> [[str]]:
        
        accs = []
        for account in accounts:
            accs += [account[0]] + [account[1:]],

        merged = []
        
        for i in range(len(accs)):
            for j in range(len(merged)):
                if accs[i][0] != merged[j][0]:
                    continue
                # print('accs[i][1] = ', accs[i][1])
                # print('merged[j][1] = ', merged[j][1])
                intersect = set(accs[i][1]) & set(merged[j][1])
                if intersect:
                    #print(accs[i][1])
                    #print(merged[j][1])
                    merged[j] = [merged[j][0]] + [list(set(set(accs[i][1]) | set(merged[j][1])))]
                    break
            else:
                merged += [accs[i][0]] + accs[i][1:],

            #print('m:', merged)

        
        res = []
        for m in merged:
            print(m)
            res += [m[0]] + m[1],
            
        self.sort(res)

        #for r in res:
            #print(r)
        return res


stime = time.time()
(Solution().accountsMerge([['A', 'Aa@mail.com', 'ab@mail.com'],
   ['A', 'aaa@mail.com'], ['A', 'Aa@mail.com'], ['B', 'b@mail.com']]))
print('elapse time: {} sec'.format(time.time() - stime))