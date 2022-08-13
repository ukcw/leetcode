from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # starting array [1,2,3,4]
        # ending array [24, 12, 8, 6]
        # if we put at each index the product of all numbers that came before it
        # [-, 1, 2, 6]
        # if we put at each index the product of all numbers that came after it
        # [24, 12, 4, -]
        # we only have to multiply each index together to obtain the result

        resultArrLeft = [1 for _ in range(len(nums))] # we establish a multiplication identity

        for n in range(1,len(nums)):
            resultArrLeft[n] = resultArrLeft[n-1] * nums[n-1]

        resultArrLeft = [1 for _ in range(len(nums))] # we establish a multiplication identity
        for n in range(-2, -len(nums)-1, -1):
            resultArrLeft[n] = resultArrLeft[n+1] * nums[n+1]

        return [resultArrLeft[i] * resultArrLeft[i] for i in range(len(resultArrLeft))]

class SpaceOptimisedSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        resultArr = [1 for _ in range(len(nums))] # we establish a multiplication identity

        for n in range(1,len(nums)):
            resultArr[n] = resultArr[n-1] * nums[n-1]

        mult = 1
        for n in range(-2, -len(nums)-1, -1):
            mult *= nums[n+1]
            resultArr[n] = resultArr[n] * mult

        return resultArr

