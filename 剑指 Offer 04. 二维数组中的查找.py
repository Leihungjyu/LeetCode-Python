# 二分查找
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                # 二分查找
                left, right = 0, len(matrix[i]) - 1
                while left <= right:
                    mid = (right - left >> 1) + left
                    if matrix[i][mid] < target:
                        left = mid + 1
                    elif matrix[i][mid] > target:
                        right = mid - 1
                    else:
                        return True
        return False

# 线性查找
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False
