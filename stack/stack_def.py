class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()     
        except IndexError:
            print("Stack is empty now")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty now")
        
    def __len__(self):
        return len(self.items)

    # __str__도 있는데 무슨 뜻이었더라