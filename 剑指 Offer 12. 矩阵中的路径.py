class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if k == len(word):
                return True
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[k]:
                    board[x][y] = ""
                    if dfs(x, y, k+1):
                        return True
                    board[x][y] = word[k]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = ""
                    if dfs(i, j, 1):
                        return True
                    board[i][j] = word[0]
        return False
