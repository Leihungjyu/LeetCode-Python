class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True
        return False

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i] and matrix[i][0] <= target and matrix[i][-1] >= target:
                left, right = 0, len(matrix[0]) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[i][mid] <  target:
                        left = mid + 1
                    elif matrix[i][mid] > target:
                        right = mid - 1
                    else:
                        return True
        return False
