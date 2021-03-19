class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

class Solution:
    def reverseWords(self, s: str) -> str:
        start = end = len(s) - 1
        ans = []

        while start >= 0:
            while start >= 0 and s[start] != " ":
                start -= 1
            if s[start+1:end+1]:
                ans.append(s[start+1:end+1])
            while start >= 0 and s[start] == " ":
                start -= 1
            end = start
        return " ".join(ans)
