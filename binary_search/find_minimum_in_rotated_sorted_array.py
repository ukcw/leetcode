class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0

        while left <= right:
            mid = left + (right-left) // 2

            if nums[mid] >= nums[left]:
                if nums[right] < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # nums[mid] < nums[left]
                if mid > 0 and nums[mid-1] > nums[mid]:
                    break
                else:
                    right = mid - 1

        return nums[mid]

    def elegantSolution(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # search right side
                left = mid + 1
            else:
                # search left side
                right = mid - 1

        return nums[left]
