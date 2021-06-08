# 内置函数
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")

# 遍历替换
class Solution:
    def replaceSpace(self, s: str) -> str:
        return "".join(char if char != " " else "%20" for char in s)
