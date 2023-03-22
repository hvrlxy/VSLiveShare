'''
PROBLEM 2:

Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node 
values in the path equals targetSum. Each path should be 
returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and 
ending at any leaf node. A leaf is a node with no children.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def pathSum(self, root, targetSum):
        res = []
        
        def dfs(root,targetSum,path):
            if not root :
                return 
            if root.left is None and root.right is None and targetSum - root.val == 0 :
                res.append(path + [root.val])
            dfs(root.left,targetSum - root.val , path + [root.val])
            dfs(root.right,targetSum - root.val , path + [root.val])
        
        dfs(root,targetSum,[])
        return res