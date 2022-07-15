# 3.3 Implement a SetOfStacks data structure that mimics a stack of plates.

class SetOfStacks():
    def __init__(self):
        self.stacks = []
        self.cap = 3
        self.sizes = []
        self.num_stacks = 0
    def push(self, value):
        if not self.stacks or self.sizes[self.num_stacks - 1] == self.cap:
            self.num_stacks += 1
            self.sizes.append(1)
            self.stacks.append([value])
        else:
            self.stacks[self.num_stacks - 1].append(value)
            self.sizes[self.num_stacks - 1] += 1
    def pop(self):
        item = self.stacks[self.num_stacks - 1].pop()
        if not self.stacks[self.num_stacks - 1]:
            self.stacks.pop()
            self.sizes.pop()
            self.num_stacks -= 1
            print("DELTED STACK")
    # def popAt(self):
    def isEmpty(self):
        return not self.stacks
    def peek():
        return self.stacks[self.num_stacks - 1]

plates = SetOfStacks()
