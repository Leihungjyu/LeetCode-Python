class Solution:
    def reverse(self, x: int) -> int:
        tmp = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])
        return tmp if -2147483648 <= tmp <= 2147483647 else 0
