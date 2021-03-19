class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
    
        m = len(matrix)
        n = len(matrix[0])
        count = m * n
        left = 0
        right = n - 1
        top = 0
        bot = m - 1
        ans = []

        while count:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
                count -= 1
            top += 1
            for i in range(top, bot+1):
                ans.append(matrix[i][right])
                count -= 1
            right -= 1
            if top <= bot:
                for i in range(right, left-1, -1):
                    ans.append(matrix[bot][i])
                    count -= 1
                bot -= 1
            if left <= right:
                for i in range(bot, top-1, -1):
                    ans.append(matrix[i][left])
                    count -= 1
                left += 1
            
        return ans
