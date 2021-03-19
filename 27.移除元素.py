class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leng = 0
        for num in nums:
            if num != val:
                nums[leng] = num
                leng += 1
        return leng

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        
        return left
