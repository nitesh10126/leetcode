"""
29. Divide Two Integers
Attempted
Medium
Topics
Companies
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.



Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.


Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_sign = -1 if dividend < 0 else 1
        divisor_sign = -1 if divisor < 0 else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0
        if dividend == divisor:
            return dividend_sign * divisor_sign
        
        result = 0
        while(divisor <= dividend):
            temp_divisor = divisor
            quotient = 1
            while(temp_divisor <= dividend):
                dividend -= temp_divisor
                result += quotient
                temp_divisor += temp_divisor
                quotient += quotient
        
        if dividend_sign != divisor_sign:
            result = -1 * result

        if result > 2**31-1:
            return 2**31-1
        if result < -1*(2**31):
            return -1*(2**31)

        return result





        quotient = 1
        total = divisor
        dividend_left = dividend - total
        result = quotient
        while(dividend_left > 0):
            if dividend_left - (total+total) >= 0:
                total = total + total
                quotient = quotient + quotient
                result += quotient
                dividend_left = dividend_left - total
            elif dividend_left - divisor >= 0:
                total = divisor
                quotient = 1
                result += quotient
                dividend_left -= total
            elif dividend_left < divisor:
                dividend_left = 0

            if result > 2**31 - 1:
                return 2*31 - 1
            if result < -1*(2**31):
                return -1*(2**31))
        return (divisor_sign*dividend_sign)*result
            





































