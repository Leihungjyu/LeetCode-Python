class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                left = 0
                right = n - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[i][mid] > target:
                        right = mid - 1
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        return True
                return False
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid//n][mid%n] > target:
                right = mid - 1
            elif matrix[mid//n][mid%n] < target:
                left = mid + 1
            else:
                return True
        return False
