class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.data:
            return -1
        return self.data.pop()

    def size(self):
        return len(self.data)

    def empty(self):
        if not self.data:
            return 1
        return 0

    def top(self):
        if not self.data:
            return -1
        return self.data[-1]

# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(
def vps():
    tc = int(input())
    for i in range(tc):
        instr = input()
        stack = Stack()
        state = 'YES'
        for ch in instr:
            if ch == '(':
                stack.push(ch)
            elif ch == ')':
                li = stack.pop()
                if -1 == li:
                    state = 'NO'
                    break
        if 0 == stack.empty():
            state = 'NO'
        print(state)


# (), [], (()), ([]) 등은 올바른 괄호열
# 점수
# ()는 2점
# []는 3점
# (X)는 2*X점
# [X]는 3*X점
# ()[]는 2 + 3점

# 1이상 30이하의 input string에 대해 계산
# 올바르지 못한 괄호열이면 0을 출력

# (()[[]])([]) 
# 28

def value_parenthesis_set(in_str):
    stack = Stack()
    state = 'YES'
    pre_op = None
    tot_score = []
    item_queue = []
    sub_total_score = 0

    for ch in in_str:
        # print('score = ', sub_total_score)
        # print('stack = ', stack.data)
        # print('itemq = ', item_queue)
        # print('this = ', ch)
        # print('tot_score = ', sum(tot_score), end = '\n\n')
        if not (ch == '(' or ch == ')' or ch == '[' or ch == ']'):
            state = 'NO'
            break
        if ch == '(' or ch == '[':
            stack.push(ch)
            pre_op = 'push'
        elif ch == ')' or ch == ']':
            li = stack.pop()
            if ((-1 == li) or (li == '(' and ch != ')') 
                or (li == '[' and ch != ']')):
                state = 'NO'
                break
            if ch == ')':
                score = 2
            elif ch == ']':
                score = 3

            if 'push' == pre_op:    # elem
                item_queue.append(score)
                if 1 == stack.empty():
                    tot_score.append(item_queue.pop(0))
            else:
                if 1 != stack.empty():
                    score *= item_queue.pop()
                    item_queue.append(score)
                else:
                    #print('iq = ', item_queue, ' score = ', score)
                    sub_total_score = 0
                    while item_queue:
                        sub_total_score += item_queue.pop(0)
                    sub_total_score *= score
                    tot_score.append(sub_total_score)
            pre_op = 'pop'

    if 0 == stack.empty():
        state = 'NO'
    while item_queue:
        tot_score.append(item_queue.pop())
    #print(state)
    if 'NO' == state:
        print(0)
    else:
        print(sum(tot_score))


#in_str = '(()[[]])([])'      # 22 + 6 = 28
#in_str = '(((())))'         # 16
#in_str = '(())(())()[()]'   # 16
         # 4 + 4 + 2 + 6
         # 
#in_str = '()(())'  # 6
in_str = input()
value_parenthesis_set(in_str)

