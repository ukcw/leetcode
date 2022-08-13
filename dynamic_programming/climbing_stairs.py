class Solution:
    def climbStairs(self, n: int) -> int:
        # example of n = 5
        # from 5 there is 1 step to reach 5
        # from 4 there is 1 step to reach 5
        # from 3 we can reach 4 or 5, which means we have 1 + 1 = 2 ways of reaching 5
        # from 2 we can reach 3 or 4, which means we have 2 + 1 = 3 ways of reaching 5
        # from 1 we can reach 2 or 3, which means we have 3 + 2 = 5 ways of reaching 5
        # from 0 we can reach 1 or 2, which means we have 5 + 3 = 8 ways of reaching 5
        first = second = 1

        for _ in range(n-1):
            first, second = first + second, first

        return first
