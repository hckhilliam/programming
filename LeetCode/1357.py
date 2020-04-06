class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
      self.n = n
      self.discount = discount
      self.products = {products[i]: prices[i] for i in range(len(products))}
      self.customers = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
      self.customers += 1
      cost = sum(self.products[product[i]] * amount[i] for i in range(len(product)))
      if self.customers % self.n == 0:
        cost -= (cost * self.discount) / 100.0
      return cost
