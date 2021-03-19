class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        table = {}
        for i in s:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        for j in t:
            if j in table:
                table[j] -= 1
                if table[j] == -1:
                    return j
            else:
                return j
                
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sums = 0
        sumt = 0
        for i in s:
            sums += ord(i)
        for j in t:
            sumt += ord(j)
        return chr(sumt-sums)