from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = {}

        for s in strs:
            sortedS = tuple(sorted(s))

            groupDict[sortedS] = groupDict.get(sortedS, []) + [s]

        return groupDict.values()
