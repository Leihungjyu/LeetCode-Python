class Solution:
    def max_heap(self, nums, root, size):
        left = root * 2 + 1
        right = left + 1
        larger = root
        if left < size and nums[left] > nums[larger]:
            larger = left
        if right < size and nums[right] > nums[larger]:
            larger = right
        if larger != root:
            nums[root], nums[larger] = nums[larger], nums[root]
            self.max_heap(nums, larger, size)

    def build_max_heap(self, nums):
        for i in range(len(nums)//2-1, -1, -1):
            self.max_heap(nums, i, len(nums))
    
    def k_largest(self, nums, k):
        largest = 0
        for i in range(k):
            nums[0], nums[-1] = nums[-1], nums[0]
            largest = nums.pop()
            self.max_heap(nums, 0, len(nums))
        return largest

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.build_max_heap(nums)
        return self.k_largest(nums, k)
        
class Solution:
    def min_heap(self, nums, root, k):
        smaller = root
        left = root * 2 + 1
        right = left +1
        if left < k and nums[left] < nums[smaller]:
            smaller = left
        if right < k and nums[right] < nums[smaller]:
            smaller = right
        if smaller != root:
            nums[smaller], nums[root] = nums[root], nums[smaller]
            self.min_heap(nums, smaller, k)
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k//2-1, -1, -1):
            self.min_heap(nums, i, k)
        for j in range(k, len(nums)):
            if nums[j] > nums[0]:
                nums[j], nums[0] = nums[0], nums[j]
                self.min_heap(nums, 0, k)
        return nums[0]
