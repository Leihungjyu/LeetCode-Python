class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def func(root):
            if not root:
                return
            func(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
            func(root.left)
            
        self.k = k
        func(root)

        return self.ans
