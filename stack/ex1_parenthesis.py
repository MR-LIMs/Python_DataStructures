# 괄호 쌍 맞추기
"""
Parenthesis : ()
Brace : {}
Bracket : []
Chevron : <>
"""
"""
input : 괄호의 문자열 / ex. "()())("
output : 괄호 쌍이 맞으면 True, 짝이 안맞으면 False
         ex. "()()()" : True / "())(" : False
"""
"""
Solution
- (가 오면 stack에 push
- )가 오면 stack에서 pop 

- 빈 stack에 )가 오면 False
- stack에 (가 남아있으면 False
- 끝까지 마쳤을 때, 정상적으로 stack이 비어있으면 True
"""
import stack_def as st

s = st.Stack()

parenthesis = input("괄호를 입력하세요 : ")

def checkPar(): # 인자로 parenthesis 안 넣어도 되나?
    for p in parenthesis:
        if p == '(':
            s.push(p)
        elif p == ')':
            s.pop()
            if IndexError:
                print("Incorrect pair parenthesis1")
                return False
        else:
            print("not allowed Symbol")
            return False
    if len(s)>0:
        print("Incorrect pair parenthesis2")
        return False
    else:
        print("corret pair parenthesis")
        return True

print(checkPar())
        