# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        grid = ['' for r in range(numRows)]
        i, r = 0, 0

        while i < len(s):
            r %= numRows

            # Place the letters to be straight down in each row
            while r < numRows:
                grid[r] += s[i]
                i += 1
                r += 1

                # If we run out of letters in s
                if i >= len(s):
                    break

            # Number of letters in the upward incline
            inclineR = numRows - 2

            # From last row to top
            # Upto 0 only -> not including 0th row.
            # 0th row is start of the straight down letters
            for inc in range(inclineR, 0, -1):
                if i < len(s):
                    grid[inc] += s[i]
                    i += 1

        return ''.join(grid)


'''
R1      R2          R3
"PAHN"	"APLSIIG"	"YIR"
'''
