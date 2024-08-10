'''
Difficulty: Easy
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

https://leetcode.com/problems/subtree-of-another-tree/description/
'''

#Method-1: Brute force
'''
In T1, traverse thorugh each node and check if node value is equal to T1 root value
If yes, then check if both trees are same or not  by starting from the curr node in T1 
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # Helper function to check if 2 trees are same or not
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        q = deque([root])

        while q:
            curr = q.popleft()
            if curr.val == subRoot.val:
                if self.isSameTree(curr, subRoot):
                    return True
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False

#Time: O(T1 * T2)
#Space: O(T1 + T2)

#------------------------------------------------------------------------------------------------

#Method-2:
'''
Similar approach to method-1, but instead of using queue, use recursion
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

