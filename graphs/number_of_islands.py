class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        MAX_ROW_LEN = len(grid)
        MAX_COL_LEN = len(grid[0])

        self.islands = 0

        def dfs(r, c, found):
            if grid[r][c] == '#' or grid[r][c] == '0':
                return

            grid[r][c] = '#'

            if not found:
                self.islands += 1
                found = True

            if r - 1 >= 0:
                dfs(r - 1, c, found)

            if r + 1 < MAX_ROW_LEN:
                dfs(r + 1, c, found)

            if c - 1 >= 0:
                dfs(r, c - 1, found)

            if c + 1 < MAX_COL_LEN:
                dfs(r, c + 1, found)

        for i in range(MAX_ROW_LEN):
            for j in range(MAX_COL_LEN):
                dfs(i,j,False)

        return self.islands
