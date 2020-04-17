class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        r = []
        ch = None
        co = {
            'a': a,
            'b': b,
            'c': c
        }

        while any(co.values()):
            if co['a'] >= co['b'] and co['a'] >= co['c'] and ch != 'a':
                r.append('a')
                co['a'] -= 1
            elif co['b'] >= co['a'] and co['b'] >= co['c'] and ch != 'b':
                r.append('b')
                co['b'] -= 1
            elif co['c'] >= co['a'] and co['c'] >= co['b'] and ch != 'c':
                r.append('c')
                co['c'] -= 1
            else:
                f = False
                for k in co:
                    if k != ch and co[k] > 0:
                        r.append(k)
                        co[k] -= 1
                        ch == None
                        f = True
                        break
                if not f:
                    break
            if len(r) >= 2 and r[-1] == r[-2]:
                ch = r[-1]
            else:
                ch = None
        return ''.join(r)
