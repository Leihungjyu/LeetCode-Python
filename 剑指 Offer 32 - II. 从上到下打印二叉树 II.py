class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, queue = [], collections.deque()
        queue.append(root)
        while queue:
            level = []   
            for _ in range(len(queue)):
                temp = queue.popleft()  
                level.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            ans.append(level)
        return ans

class Solution:
    def func(self, root, ans, dep):
        if len(ans) == dep:
            ans.append([])

        ans[dep].append(root.val)

        if root.left:
            self.func(root.left, ans, dep + 1)
        if root.right:
            self.func(root.right, ans, dep + 1)
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        self.func(root, ans, 0)
        
        return ans
