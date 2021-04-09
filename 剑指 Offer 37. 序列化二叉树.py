# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
            
        ans, deque = [], collections.deque([root])

        while deque:
            node = deque.popleft()
            if node:
                ans.append(str(node.val))
                deque.append(node.left)
                deque.append(node.right)
            else:
                ans.append("null")

        return "[" + ",".join(ans) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None

        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        deque = collections.deque([root])
        while deque:
            node = deque.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                deque.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                deque.append(node.right)
            i += 1
            
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
