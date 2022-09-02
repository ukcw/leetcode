class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(arr, l, r):
            while l >= 0 and r < len(arr) and arr[l] == arr[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        output = ""
        for i in range(len(s)):

            odd = helper(s, i, i)
            even = helper(s, i, i+1)
            if len(odd) > len(output):
                output = odd
            if len(even) > len(output):
                output = even

        return output
