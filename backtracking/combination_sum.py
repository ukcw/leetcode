class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        resultSet = []
        def backtrackSearch(candidates, currentList, target):
            if target < 0:
                return

            if target == 0:
                resultSet.append(currentList.copy())
                return

            for idx,cand in enumerate(candidates):
                currentList.append(cand)
                backtrackSearch(candidates[idx:], currentList, target - cand)
                currentList.pop()

        backtrackSearch(candidates, [], target)

        return resultSet
