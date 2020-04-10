class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = []
        self.m = []


    def push(self, x: int) -> None:
        self.d.append(x)
        if not self.m:
            self.m.append(x)
        else:
            self.m.append(min(self.m[-1], x))

    def pop(self) -> None:
        self.m.pop()
        return self.d.pop()

    def top(self) -> int:
        return self.d[-1]

    def getMin(self) -> int:
        return self.m[-1]
