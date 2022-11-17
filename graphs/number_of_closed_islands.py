class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c, val):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 1:
                return False

            grid[r][c] = 1

            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                dfs(r + x, c + y, val)

        closedIslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 or c == 0 or r == len(grid) - 1 or c == len(grid[0]) - 1:
                    dfs(r, c, 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    dfs(r, c, 1)
                    closedIslands += 1

        return closedIslands
