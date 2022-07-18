# 3.5 Write a program to sort a stack such that the smallest items are on top. You can use an additional temoprary stack, but you may not copy the elements into any other data structure.

class minStack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        if not self.stack:
            self.stack.append(value)
            return
        if self.stack[-1] >= value:
            self.stack.append(value)
            return
        tmp = []
        while self.stack and self.stack[-1] <= value:
            stack_val = self.stack.pop()
            tmp.append(stack_val)
        self.stack.append(value)
        while tmp:
            tmp_value = tmp.pop()
            self.stack.append(tmp_value)
        return
        

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
        
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def isEmpty(self):
        return  not self.stack

# ACTUAL PROBLEM - CREATE SORT ALGO FOR STACK
def minSort(stack):
    if not stack:
        return None
    sorted_stack = []
    while not stack:
        curr_val = stack.pop()
        stop_val = None
        if stack:
            stop_val = stack[-1]
        if not stop_val:
            sorted_stack.append(curr_val)
            

min_stack = minStack()
min_stack.push(1)
min_stack.push(2)
min_stack.push(-12)
min_stack.push(-13)
min_stack.push(-3)
print(min_stack.peek())
