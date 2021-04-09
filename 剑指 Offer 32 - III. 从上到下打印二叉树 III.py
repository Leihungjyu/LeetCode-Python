# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, queue = [], collections.deque([root])
        flag = -1
        
        while queue:
            level = [] 
            flag *= -1
            for _ in range(len(queue)):
                temp = queue.popleft()  
                level.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            ans.append(level[::flag])
            
        return ans
