class Trie(object):
    def __init__(self, v):
        self.v = v
        self.m = None
        self.c = {}

    def __repr__(self):
        return '{}: {}'.format(self.v, self.c)


class Solution:
    def buildTrie(self, keys):
        t = Trie('&')
        for k, v in keys:
            curr = t
            for c in k:
                if c not in curr.c:
                    curr.c[c] = (Trie(c))
                curr = curr.c[c]
            curr.m = v
        return t


    def entityParser(self, text: str) -> str:
        a = self.buildTrie([('quot;', '"'), ('apos;', "'"), ('amp;', '&'), ('gt;', '>'), ('lt;', '<'), ('frasl;', '/')])
        res = []
        i = 0
        while i < len(text):
            c = text[i]
            if c != '&':
                res.append(c)
                i += 1
                continue

            curr = a
            d = [c]
            while i + 1 < len(text) and text[i + 1] in curr.c:
                i += 1
                c = text[i]
                d.append(c)
                curr = curr.c[c]
                if curr.m:
                    d = [curr.m]
                    break
            res.extend(d)
            i += 1
        return ''.join(res)



print(Solution().entityParser('&amp; is an HTML entity but &ambassador; is not.'))
print(Solution().entityParser("and I quote: &quot;...&quot;"))
print(Solution().entityParser("Stay home! Practice on Leetcode :)"))
print(Solution().entityParser("x &gt; y &amp;&amp; x &lt; y is always false"))
print(Solution().entityParser("leetcode.com&frasl;problemset&frasl;all"))
