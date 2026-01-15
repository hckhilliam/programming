class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        openedBoxes, unopenedBoxes = self.getOpenAndUnopened(status, initialBoxes)

        totalCandies = 0
        while openedBoxes:
            box = openedBoxes.pop()  # Doesn't matter what order.
            totalCandies += candies[box]
            opened, unopened = self.getOpenAndUnopened(status, containedBoxes[box])
            openedBoxes.extend(opened)
            for unopenedBox in unopened:
                unopenedBoxes.add(unopenedBox)
            for key in keys[box]:
                status[key] = 1
                if key in unopenedBoxes:
                    unopenedBoxes.remove(key)
                    openedBoxes.append(key)

        return totalCandies

    def getOpenAndUnopened(self, status, boxes):
        opened = []
        unopened = set()
        for box in boxes:
            if status[box] == 1:
                opened.append(box)
            else:
                unopened.add(box)

        return opened, unopened
