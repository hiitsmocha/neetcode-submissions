class MinStack:
    # consider each node in the stack has its own minimum value
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_val:
            self.min_stack.append(val)
            self.min_val = val
        else:
            self.min_stack.append(self.min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        # have to update min_val after pop
        self.min_val = self.min_stack[-1] if self.min_stack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.min_stack)
        return self.min_stack[-1]
