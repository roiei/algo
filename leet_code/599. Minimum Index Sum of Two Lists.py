import time


class Solution:
    def findRestaurant2(self, list1: 'List[str]', list2: 'List[str]') -> 'List[str]':
        adict  = {}
        ml = min(len(list1), len(list2))
        if ml == len(list1):
            mlist = list1
            olist = list2
        else:
            mlist = list2
            olist = list1
        for i in range(ml):
            if mlist[i] not in adict:
                if mlist[i] in olist:
                    adict[mlist[i]] = i + olist.index(mlist[i])
        res = sorted(adict.items(), key=lambda param: param[1])
        out = []
        pval = res[0][1]
        for r in res:
            if pval != r[1]:
                break
            out.append(r[0])
        return out

    def findRestaurant(self, list1: 'List[str]', list2: 'List[str]') -> 'List[str]':
        common = set(list1) & set(list2)
        adict = {}
        for com in common:
            if com in list1 and com in list2:
                adict[com] = list1.index(com) + list2.index(com)
        res = sorted(adict.items(), key=lambda p:p[1])
        return [i[0] for i in res if res[0][1] == i[1]]


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

stime = time.time()
sol = Solution()
print(sol.findRestaurant(list1, list2)) # True
print('elapse time: {} sec'.format(time.time() - stime))