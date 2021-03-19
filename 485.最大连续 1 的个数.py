class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = count = 0
        for i in nums:
            count = count + 1 if i == 1 else 0
            maxNum = max(maxNum, count)            

        return maxNum
