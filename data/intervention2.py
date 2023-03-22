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

    def __init__(self):
        self.count = 0
        self.path = []
        self.all_paths = []

    def DFS(self, root, targetSum): 
        if root==None:
            return False
            
        count += root.val
        self.path.append(root.val)

        if root.left != None:
            newroot = root.left
            self.DFS(newroot, targetSum)
            self.count -= newroot.val
            self.path.pop(-1)
        elif root.right != None:
            newroot = root.right
            self.DFS(newroot, targetSum)
            self.count -= newroot.val
            self.path.pop(-1)
        else:
            if count==targetSum:
                self.all_paths.append(self.path)
                return True
                
            return False


def inOrder(self, root, cur_sum, targetSum):
        
        if not root: return False
        self.path.append(root.val)

        if (not root.left) and (not root.right): # leaves
            if ((cur_sum + root.val) == targetSum):
                node_vals = self.path[:]
                self.all_paths.append(node_vals)
                self.path.pop(-1)
                return True
            self.path.pop(-1)
            return False
            
        left = self.inOrder(root.left, cur_sum+root.val, targetSum) 
        right = self.inOrder(root.right, cur_sum+root.val, targetSum)
        self.path.pop(-1)
        return left or right


def pathSum(self, root, targetSum):
    """
    :type root: TreeNode
    :type targetSum: int
    :rtype: List[List[int]]
    """
    #self.DFS(root, targetSum)
    #return all_paths
    self.inOrder(root, 0, targetSum)

    return self.all_paths