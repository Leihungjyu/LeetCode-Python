class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, len(s)+n):
            res += s[i % len(s)]
        return res
