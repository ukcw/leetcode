class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(arr, l, r):
            counter = 0
            while l >= 0 and r < len(arr) and arr[l] == arr[r]:
                counter += 1
                l -= 1
                r += 1
            return counter

        output = 0
        for i in range(len(s)):

            odd = helper(s, i, i)
            even = helper(s, i, i+1)
            output += odd + even

        return output
