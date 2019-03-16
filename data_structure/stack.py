
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


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

# stack = Stack()
# tc = int(input())
# while tc > 0:
#     instr = input()
#     if -1 != instr.find('push'):
#         stack.push(int(instr[5:]))
#     elif -1 != instr.find('pop'):
#         print(stack.pop())
#     elif -1 != instr.find('size'):
#         print(stack.size())
#     elif -1 != instr.find('empty'):
#         print(stack.empty())
#     elif -1 != instr.find('top'):
#         print(stack.top())
#     tc -= 1


def check_permutation():
    a = [4, 3, 6, 8, 7, 5, 2, 1]
    #a = [5,1,2,5,3,4]

    tc = int(input())

    test_val = []
    for x in range(tc):
        test_val.append(int(input()))

    stack = Stack()

    a = test_val
    inc = 0
    cnt = 0
    for i in a:
        if inc < i:
            while inc < i:
                stack.push(inc+1)
                inc += 1
            val = stack.pop()
            cnt += 1
        else:
            val = stack.pop()
            cnt += 1
            while val > i:
                val = stack.pop()
                cnt += 1

    #print(cnt)
    if cnt != len(a):
        print('NO')
    else:
        stack = Stack()
        inc = 0
        for i in a:
            if inc < i:
                while inc < i:
                    stack.push(inc+1)
                    print('+')
                    inc += 1
                val = stack.pop()
                print('-')
            else:
                val = stack.pop()
                print('-')
                while val > i:
                    val = stack.pop()
                    print('-')
        #print(val)

# # 4, inc = 0
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)       # 4, inc = 4
# print(stack.pop())  # pop(4)

# # 3, inc = 4
# print(stack.pop())  # pop(3)

# # 6, inc = 4
# stack.push(5)       # 
# stack.push(6)  
# print(stack.pop())  # pop(6)

# # 8, inc = 6
# stack.push(7)
# stack.push(8)
# print(stack.pop())  # pop(8)

# # 7
# print(stack.pop())  # pop(7)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


