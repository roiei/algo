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

    def accountsMerge(self, accounts: [[str]]) -> [[str]]:
        """
            timeout 45/49
        """
        tbl = []
        
        for acc in accounts:
            mails = set()
            names = set()
            
            for item in acc:
                if -1 != item.find('@'):
                    mails.add(item)
                else:
                    names.add(item)
                
            tbl += [mails, names],

        for i in range(len(tbl)):
            found = False
            for j in range(i + 1, len(tbl)):
                if tbl[i][0]&tbl[j][0]:
                    tbl[j][0] = tbl[j][0]|tbl[i][0]
                    tbl[j][1] = tbl[j][1]|tbl[i][1]
                    found = True
            
            if found:
                tbl[i] = None
        
        res = []
        for item in tbl:
            if not item:
                continue
            res += list(item[1]) + sorted(item[0]),
        return res

    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        print(graph)

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []

                while stack:
                    node = stack.pop()
                    component.append(node)

                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)

                ans.append([em_to_name[email]] + sorted(component))
        return ans

    def accountsMerge(self, accounts):
        g = collections.defaultdict(set)
        names = collections.defaultdict(str)

        for acc in accounts:
            for i in range(1, len(acc)):  # 1 for only email case
                g[acc[1]].add(acc[i])
                g[acc[i]].add(acc[1])
                names[acc[1]] = acc[0]

        visited = set()
        res = []

        for email in g:
            if email in visited:
                continue

            q = [email]
            visited.add(email)
            linked_emails = [email]

            while q:
                u_email = q.pop(0)

                for v_email in g[u_email]:
                    if v_email in visited:
                        continue

                    visited.add(v_email)
                    linked_emails += v_email,
                    q += v_email,

            res += [names[email]] + sorted(linked_emails),

        return res


stime = time.time()
# print(
#     [
#     ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
#     ["John", "johnnybravo@mail.com"],
#     ["Mary", "mary@mail.com"]] == 
#     Solution().accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))


print(
    [["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co"],["Ethan","Ethan0@m.co","Ethan3@m.co"],["Gabe","Gabe0@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co"],["Kevin","Kevin2@m.co","Kevin4@m.co"]] == 
    Solution().accountsMerge([["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]))
print('elapse time: {} sec'.format(time.time() - stime))