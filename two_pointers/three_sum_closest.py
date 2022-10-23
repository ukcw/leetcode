class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        print(nums)
        for i in range(len(nums) - 2):
            j = i + 1
            r = len(nums) - 1
            while j < r:
                distance = target - (nums[i] + nums[j] + nums[r])
                if abs(distance) < abs(target - closest):
                    closest = nums[i] + nums[j] + nums[r]
                if distance < 0:
                    r -= 1
                else:
                    j += 1
        return closest
