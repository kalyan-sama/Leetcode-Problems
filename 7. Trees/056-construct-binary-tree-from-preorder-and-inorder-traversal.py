'''
Difficulty: Medium

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
'''

'''
The first element in preorder array will ALWAYS be the root node of the tree
This root element will be the pivot in the inorder traversal array. 
So, in inorder array, all the elements left to the root will be in the left portion of the tree
and all the elements right to the root will be in the right portion of the tree

So we can recursively build the tree using above properties.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        # First node in preorder list is the root
        root = TreeNode(preorder[0])

        #Get the index of root in inorder list. This is pivot index of the tree
        index = inorder.index(preorder[0])

        #Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1:index+1], inorder[:index+1])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])

        return root

#Time: O(n)
#Space: O(n)
