class Solution:
    def find_right(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1  

        return right

    def search(self, nums: List[int], target: int) -> int:
        right = self.find_right(nums, target)
        
        if not nums or nums[right] != target:
            return 0
        return right - self.find_right(nums, target-1)
