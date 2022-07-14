# 3.1 Describe how you could use a single array to implement three stacks

class arrayStack():
    def __init__(self):
        self.num_stacks = 3
        self.stack_sizes = 10
        self.arr_stack = [None] * self.num_stacks * self.stack_sizes
        self.sizes = [0] * self.num_stacks

    def pop(self, stack):
        if self.sizes[stack - 1] == 0:
            return None
        self.arr_stack[self.stack_sizes * (stack - 1) + max(self.sizes[stack - 1], 0)] = None
        self.sizes[stack - 1] -= 1
        
    def push(self, stack, value):
        if self.sizes[stack - 1] + 1 == self.stack_sizes:
            return None
        self.sizes[stack - 1] += 1
        self.arr_stack[self.stack_sizes * (stack - 1) + max(self.sizes[stack - 1], 0)] = value
        
    def peek(self, stack):
        return self.arr_stack[(self.stack_sizes * (stack - 1)) + max(self.sizes[stack - 1], 0)]

    def isEmpty(self, stack):
        return self.sizes[stack - 1] == 0

stack = arrayStack()
print(stack.isEmpty(1))
stack.push(1,1)
print(stack.isEmpty(1))
print(stack.peek(2))
print(stack.peek(3))
