# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid(root, float("-inf"), float("inf"))
    def is_valid(self, node, minn, maxx):
        if not node:
            return True
        elif node.val <= minn or node.val >= maxx:
            return False
        return self.is_valid(node.left, minn, node.val) and self.is_valid(node.right, node.val, maxx) 