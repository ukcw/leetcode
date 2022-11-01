class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])  # sort by end time
        prev = intervals[0][1]
        result = 0

        for start, end in intervals[1:]:
            if start < prev:
                result += 1
            else:
                prev = end
        return result
