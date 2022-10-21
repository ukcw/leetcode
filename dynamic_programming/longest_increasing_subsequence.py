class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = [nums[0]]

        for num in nums[1:]:
            if num <= subseq[-1]:
                replaceIndex = bisect_left(subseq, num)
                subseq[replaceIndex] = num
            else:
                subseq.append(num)

        return len(subseq)
