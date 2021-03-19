class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        ans = [root]
        while ans:
            temp = ans.pop()
            if temp and (temp.left or temp.right):
                ans.append(temp.left)
                ans.append(temp.right)
                temp.left, temp.right = temp.right, temp.left
        return root
