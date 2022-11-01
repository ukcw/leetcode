class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        output = []
        intervals.sort(key=lambda interval: interval[0])
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            i += 1
            while i < len(intervals) and intervals[i][0] <= end:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
                i += 1
            output.append([start, end])

        return output
