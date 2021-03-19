class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")

class Solution:
    def replaceSpace(self, s: str) -> str:
        return "".join(char if char != " " else "%20" for char in s)
