class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(min(0, val))

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        minim = 0 
        for i in self.minstack:
            minim = min(i, 0)    
        return minim
