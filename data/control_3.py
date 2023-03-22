# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        sum = sum - root.val
        if sum == 0 and root.left is None and root.right is None:
            return True
        # check left
        left = self.hasPathSum(root.left, sum)
        # check right
        right = self.hasPathSum(root.right, sum)
        return (left or right)