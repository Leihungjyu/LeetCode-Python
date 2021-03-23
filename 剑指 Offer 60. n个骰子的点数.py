class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        ans = [1/6] * 6
        for i in range(2, n+1):
            temp = [0] * (5 * i + 1)
            for j in range(len(ans)):
                for k in range(6):
                    temp[j+k] += ans[j] / 6
            
            ans = temp

        return ans
