class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = dict()
        maxium, left = 0, -1

        for right in range(len(s)):
            if s[right] in table:
                left = max(left, table[s[right]])
            table[s[right]] = right
            maxium = max(maxium, right-left)

        return maxium
