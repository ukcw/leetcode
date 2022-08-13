class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use two pointers:
        # l starts at index 0, r starts at index -1
        # if maxAmount is greater than current max update the max amount
        # move either l or r inwards, depending on which bar is taller
        # we move the shorter bar inwards (because if we keep it, there is
        # no way that we get a larger container amount)

        maxAmount = 0
        l, r = 0, len(height)-1

        while l < r:
            currentAmount = min(height[l], height[r]) * (r - l)

            maxAmount = max(maxAmount, currentAmount)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxAmount
