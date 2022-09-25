from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currentSum = nums[0]
        for i in nums[1:]:
            currentSum = max(i, currentSum + i)
            maxSum = max(maxSum, currentSum)
        return maxSum
