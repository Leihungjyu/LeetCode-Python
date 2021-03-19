class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        return False if len(set([x for x in nums if x]))+nums.count(0) != 5 else max(nums)-min([x for x in nums if x]) < 5

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        poker_set = set()
        min_card, max_card = 14, 0

        for num in nums:
            if num != 0:
                if num in poker_set:
                    return False
                poker_set.add(num)
                if num > max_card:
                    max_card = num
                if num < min_card:
                    min_card = num
                    
        return max_card - min_card < 5
