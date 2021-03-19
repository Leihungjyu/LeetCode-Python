class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1
                # return min(numbers[left:right+1])
        
        return numbers[left]
