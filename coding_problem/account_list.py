
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

    def print(self, merged):
        for item in merged:
            print(item)
        print()

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
            cnts = {}
            for j in range(len(merged[i])):
                if merged[i][j] not in cnts:
                    cnts[merged[i][j]] = merged[i].count(merged[i][j])

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
            print(merge_cnt)
            if 0 == merge_cnt:
                break
            accounts = mergeds

        self.remove_duplicate(mergeds)
        self.sort(mergeds)
        return mergeds


accounts = [[
        "John",                  #← name
        "johnsmith@mail.com",    #← 해당 계정의 email들
        "john00@mail.com"
    ],
    [   "John", 
        "johnnybravo@mail.com"],
    [   "John", 
        "johnsmith@mail.com",
        "john_newyork@mail.com"],
    [   "Mary", 
        "mary@mail.com"]
]

[
    [
        "John",                   #← 이름
        'john00@mail.com',        #← 정렬된 email들
        'john_newyork@mail.com', 
        'johnsmith@mail.com'
    ],
    [   "John", 
        "johnnybravo@mail.com"
    ], 
    [   "Mary", 
        "mary@mail.com"
    ]
]


accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]

# expected output
[["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]

# my output
[
["David","David0@m.co","David1@m.co","David2@m.co"],
["David","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]


s = Solution()
print(s.accountsMerge(accounts))

