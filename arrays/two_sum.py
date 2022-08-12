class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}

        for idx, n in enumerate(nums):
            if target-n in need:
                return [need[target-n], idx]
            need[n] = idx
