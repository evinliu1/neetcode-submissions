class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.sorted_stack.append(val)
        self.sorted_stack.sort()

    def pop(self) -> None:
        val = self.stack.pop()
        self.sorted_stack.remove(val)
        self.sorted_stack.sort()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.sorted_stack[0]

        
