class Solution:
    def translateNum(self, num: int) -> int:
        pre, cur = 1, 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            cur, pre = pre + cur if 10 <= x * 10 + y <= 25 else cur, cur
            y = x
        return cur
