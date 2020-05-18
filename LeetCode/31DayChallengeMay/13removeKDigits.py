from collections import defaultdict

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        d = defaultdict(list)
        for i, n in enumerate(num):
            d[int(n)].append(i)

        anchor = 0
        i = 0
        s = ""
        # print(num)
        while k > 0 and i < 10 and len(num) - anchor > k:
            a = d[i]
            j = 0
            i += 1
            while k > 0 and j < len(a):
                n = a[j]

                # print('Assessing {}'.format(num[n]))

                # Old numbers.
                if n < anchor:
                    j += 1
                    continue

                diff = n - anchor
                # Getting rid of too much.
                if k < diff:
                    break

                # print(n, num[n], anchor, diff)
                k -= diff
                # Don't add leading zeroes.
                if s or num[n] != '0':
                    s += num[n]
                anchor = n + 1
                i = 0
                break

        if k == 0:
            s += num[anchor:]
        # print(s, k, anchor)
        return s if s else '0'

# 0123503032023230420
# 000000000000001
