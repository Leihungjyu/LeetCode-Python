class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        match = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for i in s:
            if i in match:
                stack.append(i)
            elif stack == [] or match[stack.pop()] != i:
                return False
        return stack == []
