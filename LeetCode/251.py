class Vector2D:
    def __init__(self, vec: List[List[int]]):
        print(vec)
        self.vec = vec
        self.y = 0
        self.x = -1
        if len(self.vec):
            self.__advanceCursor()

    def next(self) -> int:
        curr = self.vec[self.y][self.x]
        self.__advanceCursor()
        return curr

    def __advanceCursor(self):
        self.x += 1
        if self.x == len(self.vec[self.y]):
            self.y += 1
            while self.y < len(self.vec) and not len(self.vec[self.y]):
                self.y += 1
            self.x = 0

    def hasNext(self) -> bool:
        return self.y < len(self.vec) and self.x < len(self.vec[self.y])


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
