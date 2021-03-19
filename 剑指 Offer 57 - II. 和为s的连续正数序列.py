class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right, sums, ans = 1, 2, 3, []
        while left < right:
            if sums < target:
                right += 1
                sums += right
            elif sums > target:
                sums -= left
                left += 1
            else:
                ans.append(list(range(left, right+1)))
                sums -= left
                left += 1

        return ans
