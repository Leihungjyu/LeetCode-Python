# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        headNode = ListNode(0)
        headNode.next = head

        if head == None:
            return None
        
        pre, cur = headNode, head
        while cur != None:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return headNode.next
