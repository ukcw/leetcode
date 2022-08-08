from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countDictionary = Counter(s1)
        for l in range(len(s2) - len(s1) + 1):
            if countDictionary == Counter(s2[l:l+len(s1)]):
                return True
        return False

