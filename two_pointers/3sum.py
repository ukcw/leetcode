class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we need three numbers a + b + c to equal 0
        # iterate through the sequence
        # for each number assign it as a
        # start a left pointer b at index(a) + 1
        # start a right pointer c at len(nums) - 1
        # if a + b + c = 0, then we add it to the solution set
        # if a + b + c > 0, then we move c to the left to get a smaller number
        # if a + b + c < 0, then we move b to the right to get a bigger number
        # to avoid duplicate triplets, when we move pointers a, b, and c after finding
        # a solution, we make sure to move until the number is different than before
        nums.sort()
        solutionSet = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums)-1

            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    solutionSet.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return solutionSet
