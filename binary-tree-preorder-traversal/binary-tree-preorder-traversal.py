# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = []    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if root:
        #     self.arr.append(root.val)
        #     self.preorderTraversal(root.left)
        #     self.preorderTraversal(root.right)
        # return self.arr
        stack = []
        stack.append(root)
        
        while len(stack) > 0:
            node = stack.pop()
            if node:
                self.res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        
        return self.res