class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        if not nums:
            return ans
        max_k = max(nums[:k])
        ans.append(max_k)
        for i in range(k, len(nums)):
            if nums[i-k] == max_k and nums[i] < max_k:
                max_k = max(nums[i-k+1:i+1])
            if nums[i] >= max_k:
                max_k = nums[i]
            ans.append(max_k)
        return ans

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        deque = collections.deque()
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        ans = [deque[0]]
        for i in range(k, len(nums)):
            if nums[i-k] == deque[0]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            ans.append(deque[0])
        return ans
