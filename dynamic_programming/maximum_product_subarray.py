class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = currentMax = currentMin = nums[0]
        for num in nums[1:]:
            values = (num * currentMax, num * currentMin, num)
            currentMax, currentMin = max(values), min(values)
            globalMax = max(globalMax, currentMax)
        return globalMax


# interesting linear pass solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        even length array
        [2,3,-2,4]
        forward pass: [2,6,-12,-48]
        backward pass: [-48,-24,-8,4]

        odd length array
        [2,3,-2,4,5]
        forward pass: [2,6,-12,-48, -240]
        backward pass: [-240,-120,-40,20,5]
        """
        globalMax = nums[0]
        current = 1
        for num in nums:
            current *= num
            globalMax = max(globalMax, current)
            if num == 0:
                current = 1

        current = 1
        for num in reversed(nums):
            current *= num
            globalMax = max(globalMax, current)
            if num == 0:
                current = 1

        return globalMax
