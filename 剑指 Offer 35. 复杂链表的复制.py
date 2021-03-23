class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        table = dict()
        cur = head

        while cur:
            table[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            table[cur].next = table.get(cur.next)
            table[cur].random = table.get(cur.random)
            cur = cur.next
            
        return table[head]

# 原地哈希
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        cur = head
        while cur:
            temp = Node(cur.val)
            temp.next = cur.next
            cur.next = temp
            cur = cur.next.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        pre = head
        cur = head.next
        new_head = head.next
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        
        return new_head
