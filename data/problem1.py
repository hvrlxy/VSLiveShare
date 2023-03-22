'''
PROBLEM 1:
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        ans = False
        need = targetSum - root.val

        if (need==0 and root.left is None and root.right is None):
            return True
        
        if root.left != None:
            ans = ans or self.hasPathSum(root.left, need)
        if root.right != None:
            ans = ans or self.hasPathSum(root.right, need)

        return ans
            
