# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        pos = pos_k = head
        for i in range(k):
            pos_k = pos_k.next

        while pos_k:
            pos = pos.next
            pos_k = pos_k.next
            
        return pos
