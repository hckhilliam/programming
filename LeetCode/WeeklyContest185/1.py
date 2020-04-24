class Solution:
    def reformat(self, s: str) -> str:
        chars = []
        nums = []
        for c in s:
            if c >= 'a' and c <= 'z':
                chars.append(c)
            else:
                nums.append(c)

        if abs(len(chars) - len(nums)) > 1:
            return ''

        if len(chars) >= len(nums):
            f = chars
            s = nums
        else:
            f = nums
            s = chars

        i = 0
        t = []
        while i < len(f):
            t.append(f[i])
            if i < len(s):
                t.append(s[i])
            i += 1
        return ''.join(t)


print(Solution().reformat('ec'))
print(Solution().reformat('aa1'))
print(Solution().reformat('1229857369'))
print(Solution().reformat('covid2019'))
print(Solution().reformat('ab123'))
