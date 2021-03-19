class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma = nums[0]
        pre = nums[0]
        cur = 0
        for i in range(1, len(nums)):
            cur = nums[i] + max(pre, 0)
            pre = cur
            ma = max(ma, cur)
        return ma

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)
