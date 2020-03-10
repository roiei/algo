
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Cashier:

    def __init__(self, n: int, discount: int, products: [int], prices: [int]):
        self.n = n
        self.cnt = 0
        self.discount = discount
        self.products = collections.defaultdict(int)

        for pro, price in list(zip(products, prices)):
            self.products[pro] = price


    def getBill(self, product: [int], amount: [int]) -> float:
        tot = 0
        for product, amount in list(zip(product, amount)):
            tot += amount*self.products[product]
        
        if (self.cnt + 1)%self.n == 0:
            tot = tot - (tot*self.discount/100)
        
        self.cnt += 1
        return tot
        
            
ins = zip(["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill","getBill"],
[[192,34,[77],[302]],[[77],[343]],[[77],[990]],[[77],[101]],[[77],[577]],[[77],[160]],[[77],[20]],[[77],[407]],[[77],[205]],[[77],[511]],[[77],[456]],[[77],[287]],[[77],[560]],[[77],[945]],[[77],[453]],[[77],[165]],[[77],[326]],[[77],[222]],[[77],[30]],[[77],[464]],[[77],[916]],[[77],[153]],[[77],[170]],[[77],[368]],[[77],[215]],[[77],[684]],[[77],[21]],[[77],[78]],[[77],[825]],[[77],[259]],[[77],[609]],[[77],[80]],[[77],[660]],[[77],[740]],[[77],[453]],[[77],[918]],[[77],[574]],[[77],[897]],[[77],[135]],[[77],[391]],[[77],[912]],[[77],[560]],[[77],[215]],[[77],[700]],[[77],[557]],[[77],[364]],[[77],[213]],[[77],[331]],[[77],[627]],[[77],[812]],[[77],[84]],[[77],[501]],[[77],[683]],[[77],[603]],[[77],[454]],[[77],[160]],[[77],[19]],[[77],[25]],[[77],[381]],[[77],[595]],[[77],[198]],[[77],[52]],[[77],[734]],[[77],[742]],[[77],[419]],[[77],[555]],[[77],[330]],[[77],[631]],[[77],[132]],[[77],[825]],[[77],[850]],[[77],[923]],[[77],[171]],[[77],[72]],[[77],[13]],[[77],[668]],[[77],[729]],[[77],[64]],[[77],[657]],[[77],[223]],[[77],[981]],[[77],[107]],[[77],[477]],[[77],[111]],[[77],[812]],[[77],[419]],[[77],[391]],[[77],[448]],[[77],[75]],[[77],[842]],[[77],[627]],[[77],[776]],[[77],[297]],[[77],[711]],[[77],[309]],[[77],[654]],[[77],[526]],[[77],[921]],[[77],[73]],[[77],[360]],[[77],[728]],[[77],[499]],[[77],[856]],[[77],[678]],[[77],[488]],[[77],[111]],[[77],[860]],[[77],[352]],[[77],[193]],[[77],[922]],[[77],[859]],[[77],[865]],[[77],[113]],[[77],[370]],[[77],[966]],[[77],[694]],[[77],[432]],[[77],[549]],[[77],[909]]])


obj = None
for op, param in ins:
    if op == 'Cashier':
        print(param)
        obj = Cashier(*param)
    elif op == 'getBill':
        obj.getBill(*param)
else:
    print('True')


# obj = None
# for op, param, expected in ins:
#     if op == 'Cashier':
#         obj = Cashier()
#     elif op == 'getBill':
#         if expected != obj.addWord(param):
#             print('False @ {} {} {}'.format(op, param, expected))
#             break
# else:
#     print('True')