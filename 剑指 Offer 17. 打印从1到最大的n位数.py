class Solution:
    def printNumbers(self, n: int) -> [int]:
        def func(x):
            if x == n:
                char = "".join(self.num[self.start:])
                if char != "0":
                    self.ans.append(int(char))
                if n - self.start == self.nine:
                    self.start -= 1
                return

            for i in range(10):
                if i == 9:
                    self.nine += 1
                self.num[x] = str(i)
                func(x+1)
            self.nine -= 1

        self.num, self.ans = ["0"] * n, []
        self.start, self.nine = n - 1, 0
        func(0)

        return self.ans
