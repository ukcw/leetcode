"""
Top-down memoization
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amt):
            if amt == 0:
                return 0
            if amt in memo:
                return memo[amt]
            res = float("+inf")
            for coin in coins:
                if amt - c >= 0:
                    res = min(res, 1 + dp(amt - coin))
            memo[amt] = res
            return res

        result = dp(amount)
        return result if result != float("+inf") else -1


"""
DP n * coins
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("+inf")] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    break
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("+inf") else -1
