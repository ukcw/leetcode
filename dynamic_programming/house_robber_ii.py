class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robHelper(arr):
            first = second = 0
            for n in arr:
                first, second = max(n + second, first), first
            return first
        return max(robHelper(nums[1:]), robHelper(nums[:-1]))
