class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            pop = x%10
            x //= 10
            rev = pop + rev*10
        rev *= sign
        return rev if -2**31 <= rev <= 2**31 else 0