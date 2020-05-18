class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        return self.floodFillRecurse(image, sr, sc, newColor, image[sr][sc])

    def floodFillRecurse(self, image, sr, sc, newColor, oldColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr]):
            return image

        if image[sr][sc] != oldColor:
            return image

        image[sr][sc] = newColor
        self.floodFillRecurse(image, sr - 1, sc, newColor, oldColor)
        self.floodFillRecurse(image, sr + 1, sc, newColor, oldColor)
        self.floodFillRecurse(image, sr, sc - 1, newColor, oldColor)
        self.floodFillRecurse(image, sr, sc + 1, newColor, oldColor)
        return image
