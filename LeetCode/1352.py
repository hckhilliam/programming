class ProductOfNumbers:

    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num:
            self.products.append(num * self.products[-1])
        else:
            self.products = [1]

    def getProduct(self, k: int) -> int:
        if len(self.products) <= k:
            return 0
        return self.products[-1] // self.products[-k - 1]
