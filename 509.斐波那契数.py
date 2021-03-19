class Solution:
    def fib(self, N: int) -> int:
        cur, nex = 0, 1

        while N:
            cur, nex = nex, nex + cur
            N -= 1

        return cur

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
