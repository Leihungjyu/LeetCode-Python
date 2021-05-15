class Solution:
    def romanToInt(self, s: str) -> int:
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans, cur = 0, len(s) - 1
        while cur >= 0:
            ans = ans - table[s[cur]] if cur < len(s) - 1 and table[s[cur]] < table[s[cur+1]] else ans + table[s[cur]]
            cur -= 1
        return ans
