class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        table = {}

        for i in nums2:
            if stack == []:
                stack.append(i)
            elif i > stack[-1]:
                while stack and i > stack[-1]:
                    table[stack.pop()] = i
            stack.append(i)
                
        while stack != []:
            table[stack.pop()] = -1
        for j in nums1:
            stack.append(table[j])

        return stack