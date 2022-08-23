class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        MAX_ROW_LEN = len(board)
        MAX_COL_LEN = len(board[0])

        def dfs(r, c, word, visited):
            if (r < 0
                or c < 0
                or r == MAX_ROW_LEN
                or c == MAX_COL_LEN
                or (r,c) in visited
                or board[r][c] != word[0]):
                return False

            nextWord = word[1:]
            if not nextWord:
                return True

            visited.add((r,c))
            if dfs(r + 1, c, nextWord, visited):
                return True
            if dfs(r - 1, c, nextWord, visited):
                return True
            if dfs(r, c + 1, nextWord, visited):
                return True
            if dfs(r, c - 1, nextWord, visited):
                return True
            visited.remove((r,c))

        for i in range(MAX_ROW_LEN):
            for j in range(MAX_COL_LEN):
                if dfs(i, j, word, set()):
                    return True

        return False
