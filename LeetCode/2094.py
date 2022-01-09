from collections import defaultdict

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counts = defaultdict(int)
        for d in digits:
            counts[d] += 1

        valid_nums = set()
        self.get_all(counts, [], valid_nums)
        return sorted(valid_nums)

    def get_all(self, counts, curr, valid_nums):
        if len(curr) == 3:
            num = curr[0] * 100 + curr[1] * 10 + curr[2]
            if num % 2 == 0 and num not in valid_nums:
                valid_nums.add(num)
            return

        for d, c in counts.items():
            if c > 0 and (d > 0 or curr):
                curr.append(d)
                counts[d] -= 1
                self.get_all(counts, curr, valid_nums)
                counts[d] += 1
                curr.pop()
