class Solution:
    def reverse(self, x: int) -> int:
        mark = -1 if x < 0 else 1
        if mark == -1:
            x *= -1
        x = str(x)
        x = x[::-1]
        x = int(x)
        if x > 2**31:
            return 0
        return mark * x