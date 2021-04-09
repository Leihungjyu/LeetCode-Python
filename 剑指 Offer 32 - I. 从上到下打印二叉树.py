# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
            
        ans, deque = [], collections.deque()
        deque.append(root)

        while deque:
            node = deque.popleft()
            ans.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)

        return ans
