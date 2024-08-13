'''
Difficulty: Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
 
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

https://leetcode.com/problems/validate-binary-search-tree/description/
'''

#Method-1: In order traversal
'''
For any BST, inorder traversal will be a sorted list of values.
Use inorder traversal to traverse the tree and check if it breaks theincreasing order
'''

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
        self.latest = float('-inf')
        self.ans = True
        def inorder(node):
            if node.left:
                inorder(node.left)
            if self.latest >= node.val:
                self.ans = False
            self.latest = node.val
            if node.right:
                inorder(node.right)
        inorder(root)
        return self.ans

#Time: O(n)
#Space: O(n)

#---------------------------------------------------------------------------------------------------

#Method-2: Traverse the tree normally
'''
For BST, every node in the tree will have lower and upper boundaries

for root => -inf < root.val < +inf
for left node => -inf < left.val < root.val
for right node => root.val < right.val < +inf

Traverse through every node in the tree and check if above conditions are satisfied.
'''

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
        def isValid(node, leftMax, rightMax):
            if not node:
                return True
            if not (leftMax < node.val < rightMax):
                return False
            
            return (isValid(node.left, leftMax, node.val) and
                    isValid(node.right, node.val, rightMax))
        return isValid(root, float('-inf'), float('inf'))

#Time: O(n)
#Space: O(n)
