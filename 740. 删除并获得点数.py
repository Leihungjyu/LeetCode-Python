class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnts = [0] * 10009
        n = len(nums)
        m = 0
        for x in nums:
            cnts[x] += 1
            m = max(m, x)
        f = [[0] * 2 for _ in range(m+1)]
        for i in range(1, m+1):
            f[i][1] = f[i-1][0] + i * cnts[i]
            f[i][0] = max(f[i-1][1], f[i-1][0])
        return max(f[m][0], f[m][1])
