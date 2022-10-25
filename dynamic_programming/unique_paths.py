# DFS solution
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visit = {(m - 1, n - 1): 1}

        def brute(r, c):
            if not (r >= 0 and r < m and c >= 0 and c < n):
                return 0

            if (r, c) in visit:
                return visit[(r, c)]

            visit[(r, c + 1)] = brute(r, c + 1)
            visit[(r + 1, c)] = brute(r + 1, c)
            return visit[(r, c + 1)] + visit[(r + 1, c)]

        return brute(0, 0)


# DP solution
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]
