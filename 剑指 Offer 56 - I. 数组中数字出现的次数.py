class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        m, n, x, y = 1, 0, 0, 0
        for num in nums:
            n ^= num

        while not m & n:
            m <<= 1
        
        for num in nums:
            if num & m:
                x ^= num
            else:
                y ^= num
        
        return [x, y]
