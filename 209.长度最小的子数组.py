class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if max(nums) >= target:
            return 1
        left = 0
        right = 0
        n = len(nums)
        ans = n + 1
        sums = 0
        while right < n:
            sums += nums[right]
            while sums >= target:
                ans = min(ans, right-left+1)
                sums -= nums[left]
                left += 1
            right += 1
        return 0 if ans == n + 1 else ans