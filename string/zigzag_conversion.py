class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [""] * numRows
        rowIdx = 0
        step = 1

        for letter in s:
            # if we reach index 0, we have to start moving down the rows
            if rowIdx == 0:
                step = 1
            # if we reach the last row, we have to start moving up the rows
            if rowIdx == numRows - 1:
                step = -1

            res[rowIdx] += letter
            rowIdx += step

        return "".join(res)
