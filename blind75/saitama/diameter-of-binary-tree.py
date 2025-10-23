# LeetCode's TreeNode definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # node value
        self.left = left      # left child (TreeNode or None)
        self.right = right    # right child (TreeNode or None)

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            print(left, right)
            # Diameter passing through this node
            self.diameter = max(self.diameter, left + right)
            
            # Return depth
            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(root))  # Output: 3