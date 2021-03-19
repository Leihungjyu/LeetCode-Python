class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote, ans = 0, 0

        for num in nums:
            if not vote:
                ans = num
            vote += 1 if num == ans else -1
        
        return ans
