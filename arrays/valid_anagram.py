class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = {}

        for letter in s:
            charCount[letter] = charCount.get(letter, 0) + 1

        for letter in t:
            if letter not in charCount:
                return False
            charCount[letter] -= 1

        for v in charCount.values():
            if v != 0:
                return False

        return True

class HackySolution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
