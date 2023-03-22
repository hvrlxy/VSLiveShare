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
    def __init__(self):
        self.count = 0

    def DFS(self, root, targetSum): 
        self.count += root.val
    
        if root.left != None:
            newroot = root.left
            self.DFS(newroot, targetSum)
            self.count -= newroot.val
        elif root.right != None:
            newroot = root.right
            self.DFS(newroot, targetSum)
            self.count -= newroot.val
        else:
            if self.count==targetSum:
                return True
            return False

    

    def inOrder(self, root, cur_sum, targetSum):

        if not root: return False
        
        if (not root.left) and (not root.right): # leaves
            if ((cur_sum + root.val) == targetSum):
                return True
            return False
            
        return self.inOrder(root.left, cur_sum+root.val, targetSum) or self.inOrder(root.right, cur_sum+root.val, targetSum)


    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.inOrder(root, 0, targetSum)
            
        