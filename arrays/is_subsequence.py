class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer = 0
        if not s:
            return True

        for letter in t:
            if s[sPointer] == letter:
                sPointer += 1
            if sPointer == len(s):
                return True

        return False
