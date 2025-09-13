"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Find the lowest common ancestor of two nodes in a binary tree with parent pointers.
      
        Args:
            p: First node
            q: Second node
          
        Returns:
            The lowest common ancestor node of p and q
        """
        # Create a set to store all ancestors of node p
        visited_ancestors = set()
      
        # Traverse from p to root, adding all ancestors to the set
        current_node = p
        while current_node:
            visited_ancestors.add(current_node)
            current_node = current_node.parent
      
        # Traverse from q upward until we find a node that exists in p's ancestor set
        current_node = q
        while current_node not in visited_ancestors:
            current_node = current_node.parent
          
        # The first common ancestor found is the lowest common ancestor
        return current_node
