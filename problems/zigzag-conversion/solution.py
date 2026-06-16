class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curRow, goingDown = 0, False

        for ch in s:
            rows[curRow] += ch
            # Flip direction at top or bottom
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        return "".join(rows)
