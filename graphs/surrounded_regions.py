class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return

            if board[r][c] == "O":
                board[r][c] = "S"

                for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    dfs(r + x, c + y)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0 or c == 0 or r == len(board) - 1 or c == len(board[0]) - 1:
                    if board[r][c] == "O":
                        dfs(r, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"

        return board
