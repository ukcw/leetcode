class Solution:
    def naiveSolution(self, s: str, t: str) -> str:
        '''
        This solution is correct but runs into TLE.
        '''
        minWindowLength = s
        found = False

        for l in range(len(s)):
            # set dictionary check up
            countChecker = {}
            for letter in t:
                countChecker[letter] = countChecker.get(letter, 0) + 1

            r = l
            while r < len(s):
                if s[r] in countChecker:
                    countChecker[s[r]] -= 1

                if len(tuple(filter(lambda x: x > 0,
                        countChecker.values()))) == 0:
                    if r - l + 1 <= len(minWindowLength):
                        found = True
                        minWindowLength = s[l:r+1]
                        break

                r += 1

        return minWindowLength if found else ""

    def minWindow(self, s: str, t: str) -> str:
        minWindowLength = float("Infinity")
        l = r = 0
        result = [-1, -1]
        need = {}

        # set up need dictionary with required
        # character counts
        for letter in t:
            need[letter] = need.get(letter, 0) + 1

        needCount = len(need)

        while r < len(s):
            if s[r] in need:
                need[s[r]] -= 1
                if need[s[r]] == 0:
                    needCount -= 1

            while (needCount == 0):
                if (r - l + 1) <= minWindowLength:
                    minWindowLength = r - l + 1
                    result[0] = l
                    result[1] = r+1
                if s[l] in need:
                    if need[s[l]] == 0:
                        needCount += 1
                    need[s[l]] += 1
                l += 1

            r += 1

        return s[result[0]:result[1]] if minWindowLength != float("Infinity") else ""

if __name__ == "__main__":
    s = Solution()
    print("Test Case: ADOBECODEBANC")
    print("Result:   ", s.minWindow("ADOBECODEBANC", "ABC"))
