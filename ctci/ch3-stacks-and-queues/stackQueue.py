# 3.4 Implement a Queue class which implements a queue using two stacks

class QueueStack():
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
    def push(self, value):
        if not self.push_stack:
            while self.pop_stack:
                temp_val = self.pop_stack.pop()
                self.push_stack.append(temp_val)
        self.push_stack.append(value)
    def pop(self):
        if not self.pop_stack:
            while self.push_stack:
                temp_val = self.push_stack.pop()
                self.pop_stack.append(temp_val)
        return self.pop_stack.pop()
    def isEmpty(self):
        return not self.push_stack and not self.pop_stack

stack = QueueStack()
stack.push(3)
stack.push(2)
stack.push(1)

print(stack.pop())
print(stack.pop())

stack.push(0)

print(stack.pop())
print(stack.pop())
