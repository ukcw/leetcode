from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # per usual, let's first check if our found condition
            # is met, this is when nums[mid] == target

            if nums[mid] == target:
                return mid

            # first case to consider:
            # nums[mid] < nums[left]
            # this condition means that we are looking at a rotated portion
            # of the original array. Since it is rotated, we want to
            # go left of the current midpoint ONLY if
            # 1) target > nums[right]
            # OR
            # 2) target < nums[mid]
            # otherwise, if the target does EXIST, it will be in between
            # midpoint .. to .. right

            if nums[mid] < nums[left]:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # the second and only other case to consider:
            # nums[mid] >= nums[left]
            # this condition means that we are looking at the non-rotated
            # portion of the original array. Since it is NOT rotated,
            # we want to go right of the current midpoint ONLY if
            # 1) target < nums[left]
            # OR
            # 2) target > nums[mid]
            # otherwise, if the target does EXIST, it will be in between
            # left ... to ... midpoint

            else:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

if __name__ == "__main__":
    testCaseOne = [[3,1],1]
    s = Solution()
    print("Test Case 1:",testCaseOne[0])
    print("Expected:", 1)
    print("Output:", s.search(testCaseOne[0],testCaseOne[1]))
