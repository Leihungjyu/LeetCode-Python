# 头结点和双指针
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        pre = new_head
        cur = head

        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
                return new_head.next
            else:
                pre = pre.next
                cur = cur.next

# 头结点和单指针
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        cur = new_head

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return new_head.next
            else:
                cur = cur.next

# 单指针
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        cur = head

        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return head
            else:
                cur = cur.next
