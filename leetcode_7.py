class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        sign = -1 if x<0 else 1
        x = x if x>0 else x*-1
        str_x = str(x)
        reverse_x = ""
        for i in range(len(str_x)-1, -1, -1):
            reverse_x = reverse_x + str_x[i]

        reverse_x = sign * int(reverse_x)
        if (reverse_x <= 2**31-1) & (reverse_x >= -1*2**31):
            return reverse_x
        return 0
