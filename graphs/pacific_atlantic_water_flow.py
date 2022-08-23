class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        MAX_ROW_LEN = len(heights)
        MAX_COL_LEN = len(heights[0])

        canReachPacific = set()
        canReachAtlantic = set()

        def isReachable(r, c, visited, prev):
            if (r < 0
               or c < 0
               or r >= MAX_ROW_LEN
               or c >= MAX_COL_LEN
               or (r,c) in visited
               or heights[r][c] < prev):
                return

            visited.add((r,c))
            isReachable(r + 1, c, visited, heights[r][c])
            isReachable(r - 1, c, visited, heights[r][c])
            isReachable(r, c + 1, visited, heights[r][c])
            isReachable(r, c - 1, visited, heights[r][c])

        for x in range(MAX_ROW_LEN):
            isReachable(x, 0, canReachPacific, heights[x][0])
            isReachable(x, MAX_COL_LEN-1, canReachAtlantic, heights[x][MAX_COL_LEN-1])

        for y in range(MAX_COL_LEN):
            isReachable(0, y, canReachPacific, heights[0][y])
            isReachable(MAX_ROW_LEN-1, y, canReachAtlantic, heights[MAX_ROW_LEN - 1][y])

        return canReachPacific&canReachAtlantic
