import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def get_op_prio(self, op):
        if op == '(':
            return 0
        elif op == '+' or op == '-':
            return 1;
        elif op == '*' or op == '/':
            return 2;
        return 3;

    def is_op(self, k):
        return (k == '+' or k == '-' or k == '*' or k == '/');

    def to_postfix2(self, s):
        stk = []
        i = 0
        res = []
        n = len(s)

        while i < n:
            c = s[i]
            i += 1
            if '(' == c:
                stk += c,
            elif '0' <= c <= '9':
                while i < n and '0' <= s[i] <= '9':
                    c += s[i]
                    i += 1
                stk += c,
            elif ')' == c:
                while stk and stk[-1] != '(':
                    res += stk.pop(),
                stk.pop()
            elif self.is_op(c):
                # pop all higher operators
                while stk and self.get_op_prio(stk[-1]) >= self.get_op_prio(c):
                    res += stk.pop(),
                stk += c,

        while stk:
            res += stk.pop(),
        return res

    def calc(self, postfix):
        stk = []
        try:
            while postfix:
                item = postfix.pop(0)
                if '+' == item:
                    stk += int(stk.pop())+int(stk.pop()),
                elif '-' == item:
                    right = int(stk.pop())
                    left = int(stk.pop())
                    stk += left-right,
                elif '*' == item:
                    stk += int(stk.pop())*int(stk.pop()),
                elif '/' == item:
                    right = int(stk.pop())
                    left = int(stk.pop())
                    stk += left/right,
                elif '0' <= item[0] <= '9':
                    stk += item,
        except IndexError as e:
            return False
        return stk[-1]

    def calculate(self, s: str) -> int:
        postfix = self.to_postfix2(s)
        cnt = 0
        for op in ['+', '-', '*', '/']:
            cnt += postfix.count(op)
        if 0 == cnt:
            return int(''.join(reversed(postfix)))
        ret = self.calc(postfix)
        if False == ret:
            return 0
        return ret



stime = time.time()
#print(Solution().calculate("(9568+(9040-(380+(2042-(7115)+(6294)-(4395-(5183+9744+(7746-(1099+2718))-(9370-(8561+(9302)-(7632+(8451-(1759+(7760))-(3377+5363+9093+(8332-(4492-(1151+(1165-8833+(775+(3749)+9399))+9112+(6273+(7285-(6112-(668-(7756-4316-(582+1835-(6644+690+1204-(7197+(7897))+(7009-(7262))-7782-(7858+(7644+(9461+(2224)-(7531-1095-(891+1022)+2197-(9855)))+(6663-(7417-(6158-(3610))+(1481))-(4182+(4761)))+(5017))+(9990)+(6218)))-(2904)+(5631)-(8888)+3401+(3569))+(1135))-(3695-(7713+(3479)-(9813+(8171+(8616-8026+(4634-(6973))-(9761-(623-4782)+(2514)+(6233)))))+(6140))-(6641)-8611+(8389)+8074-(4412))-(3703)+(9688+(9513))))-(4987)))+(9647)))))))))-(2299))-(4785))))))"))
print(Solution().calculate("111+999/111+999"))
#print(Solution().calculate('1+((11+12)-17)'))
#print(Solution().calculate("1-11"))
#print(Solution().calculate("2147483647"))
#print(Solution().calculate("0"))
#print(Solution().calculate("1"))
#print(Solution().calculate("(1)"))
#print(Solution().calculate("1 + 1"))
#print(Solution().calculate(" 2-1 + 2 "))
#print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
print('elapse time: {} sec'.format(time.time() - stime))