class Solution:
    def capitalizeTitle(self, title: str) -> str:
        parts = title.split(' ')
        capitalized = []
        for p in parts:
            if len(p) <= 2:
                capitalized.append(p.lower())
            else:
                capitalized.append(p.title())
        return ' '.join(capitalized)
