class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def func(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return func(left.left, right.right) and func(left.right, right.left)
        return func(root.left, root.right) if root else True
