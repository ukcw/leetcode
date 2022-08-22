from heapq import *

class MedianFinder:

    def __init__(self):
        """
        small heap | large heap

        we create two heaps, a small heap (max-heap) where the values are all
        less than or equal to all values in a large heap (min-heap).

        this allows us to have the one, or two, middle values to be accessible
        in O(1) time. if len(small) is equal to len(large), meaning we have an
        even number of elements, we sum the max value of small and the min
        value of large, and divide by two to get the average of the two middle
        values. if we instead have an odd number of elements, we return the
        min value of large.
        """
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        """
        for each element that we receive, we first push it into the large heap
        to filter the value. we do this to retain the invariant that all values
        in the small heap have to be less than or equal to all values in the
        large heap. the element that gets popped off the large heap will be the
        smallest  value in the large heap, and as such, helps to retain this
        invariant.

        if the size of the large heap is smaller than the size of the small
        heap, it means that prior to this point, we had two equal number of
        elements in both the small and large heap, hence by default, when
        receiving a new number, we add the number to the small heap, causing
        the size of the small heap to be larger than the size of the large heap
        by 1.

        we then pop this max value off the small heap and push it into the large
        heap. we do this because we choose to return the min value from the
        large heap when we have an odd number of elements.
        """
        heappush(self.small, -heappushpop(self.large, num))
        if len(self.large) < len(self.small):
            heappush(self.large, -heappop(self.small))

    def findMedian(self) -> float:
        """
        if the size of the small heap is less than the size of the large heap,
        it means that the median element in the min value of the large heap,
        we simply return this value.

        otherwise, we have an even number of elements and we return the value
        of the average of the max element in the small heap and the min element
        in the large heap.
        """
        if len(self.small) < len(self.large):
            return self.large[0]
        return (self.large[0] - self.small[0])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
