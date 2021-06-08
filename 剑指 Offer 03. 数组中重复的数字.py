# 先排序, 后遍历
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return nums[i]

# 哈希表
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        table = dict()
        for num in nums:
            if num in table:
                return num
            table[num] = num

# 就地排序
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]] #注意这里交换的顺序
