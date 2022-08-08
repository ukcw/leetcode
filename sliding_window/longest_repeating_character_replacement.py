import sys

class Solution:
    # brute-force method
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longestLength = l = r = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1

            # O(26 * n)
            highestFrequency = max(count.values())

            while (r - l - highestFrequency + 1 > k):
                count[s[l]] -= 1
                l += 1

            longestLength = max(longestLength, r - l + 1)

            r += 1

        return longestLength

    def optimisedSolution(self, s: str, k: int) -> int:
        count = {}
        highestFrequency = longestLength = l = r = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1

            highestFrequency = max(count[s[r]], highestFrequency)

            while (r - l - highestFrequency + 1 > k):
                count[s[l]] -= 1
                l += 1

            longestLength = max(longestLength, r - l + 1)

            r += 1

        return longestLength

if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement(sys.argv[1], int(sys.argv[2])))
    print(s.optimisedSolution(sys.argv[1], int(sys.argv[2])))
