# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
            if left > right:
                return None

            node = TreeNode(preorder[root])
            node.left = recur(root+1, left, dic[preorder[root]]-1)
            node.right = recur(dic[preorder[root]]-left+root+1, dic[preorder[root]]+1, right)

            return node

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        return recur(0, 0, len(inorder)-1)
