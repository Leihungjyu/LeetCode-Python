class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, maxium = float("inf"), 0
        for i in prices:
            maxium = max(maxium, i-cost)
            cost = min(cost, i)

        return maxium
