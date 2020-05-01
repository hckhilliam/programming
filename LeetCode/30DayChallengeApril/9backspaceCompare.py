class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        si = len(S) - 1
        ti = len(T) - 1
        while si >= 0 or ti >= 0:
            c = 0
            while si >= 0 and S[si] == '#':
                while si >= 0 and S[si] == '#':
                    c += 1
                    si -= 1
                while si >= 0 and c > 0 and S[si] != '#':
                    si -= 1
                    c -= 1

            c = 0
            while ti >= 0 and T[ti] == '#':
                while ti >= 0 and T[ti] == '#':
                    c += 1
                    ti -= 1
                while ti >= 0 and c > 0 and T[ti] != '#':
                    ti -= 1
                    c -= 1

            if ti < 0 or si < 0:
                break

            if S[si] != T[ti]:
                return False

            si -= 1
            ti -= 1
        return si < 0 and ti < 0
