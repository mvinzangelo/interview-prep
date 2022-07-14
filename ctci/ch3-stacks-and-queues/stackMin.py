# 3.2 How would you design a stack which, in addition to push and pop, has a function 'min' which returns the min element?Push, pop, and min should all operate in O(1) time.

class stackMin():
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def pop(self):
        top = self.stack.pop()
        if self.min_stack:
            if (top == self.min_stack[-1]):
                self.min_stack.pop()
    
    def push(self, value):
        self.stack.append(value)
        if self.min_stack:
            if (value <= self.min_stack[-1]):
                self.min_stack.append(value)
        else:
            self.min_stack.append(value)
                
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
        
    def isEmpty(self):
        return len(self.stack) == 0

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None

stack = stackMin()
stack.push(10)
stack.push(9)
print(stack.min())
stack.push(8)
stack.push(10)
stack.push(1)
print(stack.min())
stack.pop()
stack.pop()
stack.pop()
print(stack.min())

