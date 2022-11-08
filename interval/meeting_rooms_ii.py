class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # sort both start and end times into two different lists
        # maintain two pointers, one for start, one for end
        # for each start time, if the current end pointer points
        # to an end time that is smaller or equal to the current start
        # time, move the end pointer forward
        # otherwise, add a count to the number of rooms needed since
        # a meeting has not yet ended to reuse a room
        # return the number of rooms added

        start = list(map(lambda i: i[0], sorted(intervals, key=lambda i: i[0])))
        end = list(map(lambda i: i[1], sorted(intervals, key=lambda i: i[1])))

        s = e = rooms = 0

        while s < len(start):
            if start[s] >= end[e]:
                e += 1
            else:
                rooms += 1

            s += 1

        return rooms


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # sort by start times
        # use a min-heap to store each new meeting (by end time)
        # if a start time is later or equal to the earliest end time
        # delete the earliest end time from the heap and add the end
        # time of the new meeting to be scheduled
        # the final size of the heap is the number of required rooms

        intervals.sort(key=lambda i: i[0])

        import heapq

        minHeap = []

        for start, end in intervals:
            if minHeap and start >= minHeap[0]:
                heapq.heappushpop(minHeap, end)
            else:
                heapq.heappush(minHeap, end)

        return len(minHeap)
