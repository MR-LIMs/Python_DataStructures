# 계산기 코드 작성
"""
Input : operator(+-*/) + operand(숫자, 영문자)
output : result of operation
"""
"""
Solution
- list : outstack => expression을 담을 그릇
- stack : operator, operand stack => 연산자를 담을 그릇

- 1단계 : Infix expression -> postfix expression
- 2단계 : run operation
"""

from stack_def import *

outstack = []
opstack = Stack()

# operator별 우선순위 : 숫자가 낮을수록 우선순위가 높다.
def rank(operator):
    if operator == '(' or operator == ')':
        return 3
    elif operator == '*' or operator == '/':
        return 1
    elif operator == '+' or operator == '-':
        return 2
    else:
        return 4    # operand를 의미

def operation(operator, a, b):
    a = int(a)
    b = int(b)
    if operator == '*':
        return b*a
    elif operator == '/':
        return b/a
    elif operator == '+':
        return b+a
    elif operator == '-':
        return b-a
    else:
        print("uncorrect token")
        return False

def calculator(expr):
    for e in expr:
        print(e)
        # e가 operand일 경우, outstack으로 쌓기
        if rank(e) == 4:
            outstack.append(e)
        # e가 operand일 경우
        else:
            # opstack이 비어있으면, 무조건 쌓기
            if len(opstack) == 0:
                opstack.push(e)
            # opstack이 차있을 경우,
            else:
                # 쌓인 원소보다 e의 순위가 높으면 쌓기
                if rank(opstack.top()) >= rank(e):
                    opstack.push(e)
                # e가 )라면 pop
                elif e == '(':
                    opstack.push(e)
                elif e == ')':
                    opstack.push(e)
                    opstack.pop()
                    outstack.append(opstack.pop())
                    opstack.pop()
                    # outstack으로 pop된 operator를 이용해 계산
                    outstack.append(operation(outstack.pop(), outstack.pop(), outstack.pop()))
                # 쌓인 원소보다 e의 rank 값이 더 크다면 outstack으로 빼주기
                else:
                    # 우선순위가 낮을 때 or stack이 비어있을 때까지
                    while(rank(e) > rank(opstack.top()) or len(opstack) == 0):
                        outstack.append(opstack.pop())
                        # outstack으로 pop된 operator를 이용해 계산
                        outstack.append(operation(outstack.pop(), outstack.pop(), outstack.pop()))
                    opstack.push(e)

        print(outstack, opstack.items)
    print(outstack[0])
            
expr = "(1+2)*3"

calculator(expr)

"""
for t in outstack:
    if t == operand:
        opstack.push(t)
    else:
        a = opstack.pop()
        b = opstack.pop()
        opstack.push(b t a)
""" 
