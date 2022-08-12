class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the number of occurances of each number using a dictionary
        # use a List[List[int]] to group the number of occurances
        # the index of the list is mapped to the count of a number
        # e.g. if the number 2 appeared 3 times and the number
        #      8 appeared 2 times then
        #      [[],[],[8],[2]]
        # now we have a sorted list in ascending order of most frequent elements

        count = {}
        group = [[] for _ in range(len(nums) + 1)]
        result = []

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key,v in count.items():
            group[v].append(key)

        for lst in reversed(group):
            if len(lst) > 0:
                result.extend(lst)
                k -= len(lst)
            if k == 0:
                return result
