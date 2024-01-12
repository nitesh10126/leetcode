class Solution:
    # pattern based solution (not intuitive)
    def convert(self, s: str, numRows: int) -> str:
        converted_str = ""
        str_len = len(s)

        if numRows == 1:
            return s

        for row in range(numRows):
            index = row
            jump_parity = 1
            zig = 2(numRows - row - 1), zag = 2*row
            while((index < str_len) & (len(converted_str) != str_len)):
                converted_str = converted_str + s[index]
                if row in [0, numRows-1]:
                    index = index + max(zig, zag)
                else:
                    index = index + (zig if jump_parity else zag)
                    jump_parity = jump_parity^1

        return converted_str

    # intuitive soluion. It does exactly what you do to solve problem by hand.
    def convert(self, s:str, numRows: int) -> str:
        if numRows == 1:
            return s

        row_str = ["" for _ in range(numRows)]
        row = 0
        down = 1
        for letter in s:
            row_str[row] = row_str[row] + letter

            if row == 0:
                down = 1
            if row == numRows-1:
                down = 0

            if down == 1:
                row += 1
            else:
                row -= 1

        converted_str = ""
        for sub_string in row_str:
            converted_str += sub_string

        return converted_str


"""
Key Learnings:
    1. for pattern type question, it's better to draw-out pattern-indices for smaller
        values of N.
    2. write edge-cases return statement for which solution is trivial (line no. 6-7)
    3. Be very critical when using while loop, make sure that it is going into inf loop.

    #solution2
    Observe closely how you solve problem by hand, it might help develop faster/better soution.
"""
