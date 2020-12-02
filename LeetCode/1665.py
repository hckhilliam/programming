import functools

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=functools.cmp_to_key(self.cmp))
        totalEnergy = tasks[0][1]
        energy = tasks[0][1] - tasks[0][0]
        for i in range(1, len(tasks)):
            moreEnergy = tasks[i][1] - energy
            if moreEnergy > 0:
                totalEnergy += moreEnergy
                energy += moreEnergy
            energy -= tasks[i][0]
        return totalEnergy

    def cmp(self, x, y):
        xVal = max(y[1] + x[0], x[1]) # x[1] + y[0]
        yVal = max(x[1] + y[0], y[1])
        if xVal < yVal:
            return -1
        elif xVal > yVal:
            return 1
        else:
            return 0
