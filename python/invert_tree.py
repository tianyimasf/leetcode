# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        return self.invertTree_helper(root)
    
    def invertTree_helper(self, node):
        new_node = TreeNode(node.val)
        if node.left == None and node.right == None:
            return new_node
        elif node.left == None and node.right != None:
            new_node.left = self.invertTree_helper(node.right)
            new_node.right = None
        elif node.left != None and node.right == None:
            new_node.right = self.invertTree_helper(node.left)
            new_node.left = None
        elif node.left != None and node.right != None:
            new_node.left = self.invertTree_helper(node.right)
            new_node.right = self.invertTree_helper(node.left)
        return new_node