class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.__combinationSum(candidates, set(), target)

    def __combinationSum(self, candidates, unavailable, target) -> List[List[int]]:
        combinations = []
        for candidate in candidates:
            if candidate in unavailable:
                continue

            if candidate == target:
                combinations.append([candidate])
            elif candidate < target:
                candidateCombos = self.__combinationSum(
                    candidates, set(unavailable), target - candidate
                )
                for combo in candidateCombos:
                    combo.append(candidate)
                    combinations.append(combo)

            unavailable.add(candidate)
        return combinations
