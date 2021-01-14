# pop을 정의할 때, return을 해주는 이유
a = [1, 2, 3]
print(a.pop())

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()     
            # 리스트의 pop은 삭제의 기능만 들어있나?
            # 아닌데, 왜 굳이 return을 해주는 거냐?
            # a = self.itmes.pop() => 지역함수로 작용
            # return a
        except IndexError:
            print("Stack is empty now")


# 아래 코드에서 e에 무엇을 넣든지 모두 0이 리턴된다. why?
def rank(operator):
    if operator == '(' or ')':
        return 0
    elif operator == '*' or '/':
        return 1
    elif operator == '+' or '-':
        return 2
    else:
        return 3    # operand를 의미

"""
if operator == '(' or ')':      => True
if operator == '(' or True:     => True

- 컴퓨터는 0이 아닌 모든 수는 True로 간주한다.
- 위 코드에서 if operator == '(' 는 True일수도 False일수도 있으나
- ')'는 항상 True를 의미한다.
- 따라서, if operator == '('가 True이든 False이든 
- True/False or True = True 이다.
- 결국 rank()에 인자로 무엇을 넣든 위 조건은 True가 된다.
"""