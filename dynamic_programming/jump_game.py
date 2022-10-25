class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPosition = len(nums) - 1

        for idx in range(len(nums)-1,-1,-1):
            if idx + nums[idx] >= lastPosition:
                lastPosition = idx
            print(lastPosition)
        
        return lastPosition == 0
    
     def naiveCanJump(self, nums: List[int]) -> bool:
         destination = len(nums) - 1
         if destination == 0:
             return True

         l = 0
       
         while l < destination:
             if nums[l] == 0:
                 break
             maxJump = 0
             nxtIdx = 0
             for i in range(1,nums[l] + 1):
                 furthestIndex = l + i + nums[l+i]
                 if furthestIndex >= destination:
                     return True
                 if i + nums[l+i] >= maxJump:
                     nxtIdx = l + i
                     maxJump = i + nums[l+i]
             l = nxtIdx
       
         return False
