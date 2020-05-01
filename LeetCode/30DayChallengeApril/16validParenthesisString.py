from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        lp = deque()
        w = deque()

        for i, c in enumerate(s):
            if c == '(':
                lp.append(i)
            elif c == ')':
                if lp:
                    lp.pop()
                elif w:
                    w.popleft()
                else:
                    return False
            else:
                w.append(i)

        while lp:
            if not w or lp.pop() > w.pop():
                return False

        return True

print(Solution().checkValidString('()'))
print(Solution().checkValidString('(*)'))
print(Solution().checkValidString('(*))'))
