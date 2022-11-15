class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxSquareLen = 0
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1
                if dp[r][c] > maxSquareLen:
                    maxSquareLen = dp[r][c]

        return maxSquareLen * maxSquareLen
