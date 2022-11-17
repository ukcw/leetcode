class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return

            currentIsland.add((r - row_origin, c - col_origin))

            grid[r][c] = 0

            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + x, c + y)

        distinctIslands = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                currentIsland = set()
                row_origin = r
                col_origin = c
                if grid[r][c] == 1:
                    dfs(r, c)
                    distinctIslands.add(tuple(currentIsland))

        return len(distinctIslands)
