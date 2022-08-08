import sys

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        indices = {}
        length = l = r = 0

        while r < len(s):
            # first check if the current character is in the dictionary
            # if found, we have a duplicate situation
            # if the saved index of the current character is greater than
            # the current position of the left pointer, we set the left
            # pointer to the saved index plus one.

            # if the left pointer's current position is greater than the saved
            # index of the current character, it means that we have previously
            # encountered a duplicate situation, IF we now move the left
            # pointer backwards, we will be including a duplicate section and
            # our substring will no longer be valid.

            if s[r] in indices and indices[s[r]] + 1 > l:
                l = indices[s[r]] + 1

            indices[s[r]] = r

            length = max(length, r - l + 1)

            r += 1

        return length

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring(sys.argv[1]))
