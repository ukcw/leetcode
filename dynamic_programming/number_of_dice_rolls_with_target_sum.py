class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}

        def dp(d, target):
            if d == 0:
                return 0 if target != 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]
            res = 0
            for i in range(max(0, target - k), target):
                res += dp(d - 1, i)
            memo[(d, target)] = res
            return res

        return dp(n, target) % (10**9 + 7)
