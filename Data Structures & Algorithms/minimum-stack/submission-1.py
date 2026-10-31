class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(min(val, self.minstack[-1]) if self.minstack else val)

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()
            self.minstack.pop()

    def top(self) -> int:
        if len(self.stack):
            return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minstack[-1]
