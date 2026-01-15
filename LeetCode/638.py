class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        return self.__getBestDeal(price, special, 0, needs)

    def __getBestDeal(self, price, special, specialInd, needs) -> int:
        bestDeal = 0
        for i in range(len(needs)):
            bestDeal += needs[i] * price[i]

        for i in range(specialInd, len(special)):
            s = special[i]
            leftoverNeeds = self.__getLeftovers(needs, s)
            if not leftoverNeeds:
                continue

            bestDeal = min(
                bestDeal,
                s[-1] + self.__getBestDeal(price, special, i, leftoverNeeds),
            )

        return bestDeal

    # Returns None if invalid.
    def __getLeftovers(self, needs, s) -> List[int]:
        needs = list(needs)
        for i in range(len(needs)):
            needs[i] -= s[i]
            if needs[i] < 0:
                return None
        return needs
