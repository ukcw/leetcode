class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0

        totalLength = len(nums1) + len(nums2)
        even = True if totalLength % 2 == 0 else False
        median = totalLength // 2

        n1 = 0
        n2 = 0

        res = []
        while n1 < len(nums1) and n2 < len(nums2):
            totalIndex = n1 + n2
            if nums1[n1] <= nums2[n2]:
                res.append(nums1[n1])
                n1 += 1
            else:
                res.append(nums2[n2])
                n2 += 1
            
            if not even and totalIndex == median:
                return res[-1]
            if even and totalIndex == median:
                return (res[-1] + res[-2])/2
        
        while n1 < len(nums1):
            totalIndex = n1 + n2
            res.append(nums1[n1])
            n1 += 1
            if not even and totalIndex == median:
                return res[-1]
            if even and totalIndex == median:
                return (res[-1] + res[-2])/2
        
        while n2 < len(nums2):
            totalIndex = n1 + n2
            res.append(nums2[n2])
            n2 += 1
            if not even and totalIndex == median:
                return res[-1]
            if even and totalIndex == median:
                return (res[-1] + res[-2])/2
