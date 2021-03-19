class Solution:
    def firstUniqChar(self, s: str) -> str:
        table = dict()
        for char in s:
            table[char] = not char in table
        for k, v in table.items():
            if v:
                return k
        return " "
