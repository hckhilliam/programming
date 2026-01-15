class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        finalParagraph = []
        currLineWords = [words[0]]
        leftoverWidth = maxWidth - len(words[0])
        for w in words[1:]:
            # add 1 to account for at least one space
            if len(w) + 1 > leftoverWidth:
                s = self.createString(currLineWords, leftoverWidth)
                finalParagraph.append(s)
                currLineWords = [w]
                leftoverWidth = maxWidth - len(w)
            else:
                currLineWords.append(w)
                # at least 1 space + word.
                leftoverWidth -= 1 + len(w)

        s = " ".join(currLineWords) + (" " * leftoverWidth)
        finalParagraph.append(s)
        return finalParagraph

    def createString(self, currLineWords, leftoverWidth):
        # split leftoverWidth to spaces and reset to new line.
        if len(currLineWords) == 1:
            s = currLineWords[0] + (" " * leftoverWidth)
        else:
            # 1 space already accounted for in caluclations.
            spacePer = (leftoverWidth // (len(currLineWords) - 1)) + 1
            extraSpaces = leftoverWidth % (len(currLineWords) - 1)

            regSpace = " " * spacePer
            extraSpace = " " * (spacePer + 1)

            s = currLineWords[0]
            for ww in currLineWords[1:]:
                if extraSpaces:
                    s += extraSpace + ww
                    extraSpaces -= 1
                else:
                    s += regSpace + ww
        return s
