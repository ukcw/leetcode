class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = {}

        # initialize grids
        for i in range(9):
            grid[i] = []

        def isValidRow(row: List[int]) -> bool:
            seen = set()
            for num in row:
                if num in seen and num != '.':
                    return False
                seen.add(num)
            
            return True

        def collectColumns(board: List[List[int]]) -> List[List[int]]:
            columns = [[] for _ in range(len(board))]

            for rdx, row in enumerate(board):
                for idx, num in enumerate(row):
                    # rowIndex // 3 * 3 + colIndex // 3 gives us grid number
                    grid[rdx//3 * 3 + idx//3].append(num)
                    columns[idx].append(num)

            return columns
        
        # check rows
        for row in board:
            if not isValidRow(row):
                return False
        
        # check cols
        for col in collectColumns(board):
            if not isValidRow(col):
                return False

        # check grids
        for row in grid.values():
            if not isValidRow(row):
                return False

        return True
