class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return [] if not head else self.reversePrint(head.next) + [head.val] 

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
