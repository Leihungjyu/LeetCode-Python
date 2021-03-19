# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def func(root):
            return 0 if not root else max(func(root.left), func(root.right)) + 1
        return True if not root else abs(func(root.left) - func(root.right)) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def func(root):
            if not root:
                return 0
            left = func(root.left)
            if left == -1:
                return -1
            right = func(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return func(root) != -1
