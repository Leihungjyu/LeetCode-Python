# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def recur(root, target):
            if not root:
                return None

            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, target)
            recur(root.right, target)
            path.pop()

        res, path = [], []
        recur(root, target)

        return res
