class Solution:
    def minNumber(self, nums: List[int]) -> str:
        return "".join(map(str, sorted(nums, key=lambda x: x/(10**len(str(x))-1))))
