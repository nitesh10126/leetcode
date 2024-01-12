class Solution:
    def intToRoman(self, num: int) -> str:
        lookup_table = {
            1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 
            20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60:'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C',
            200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M'
        }
        roman = ''
        for position in [1000, 100, 10, 1]:
            if num <= 0:
                continue

            digit = int(num/position)
            if digit == 0:
                continue

            digit_pos = digit * position
            if digit_pos in lookup_table:
                roman = roman + lookup_table[digit_pos]
            else:
                roman = roman + digit*lookup_table[position]

            num = num - digit_pos
            
        return roman

"""
O(n) solution where n is digits in number.
Don't shy away from using lookup table whereever it gives simpler solution. Above lookup table has just 30 keys and is covering 3999 cases.
"""
