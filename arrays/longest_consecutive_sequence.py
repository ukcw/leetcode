class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        maxSeqLen = 0 # minimum length

        for n in nums:
            # if n-1 is in the numsSet, then we do not iterate upwards
            # if n-1 is not in numsSet, then we check the sequence length
            # we simply walk each subsequence of numbers once

            if n-1 not in numsSet:
                seqLen = 1
                while n+1 in numsSet:
                    seqLen += 1
                    n += 1

                maxSeqLen = max(maxSeqLen, seqLen)

        return maxSeqLen
