class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        first = second = 0

        for n in nums:
            first, second = max(first, n + second), first

        return first
