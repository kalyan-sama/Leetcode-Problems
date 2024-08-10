'''
Difficulty: Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 
https://leetcode.com/problems/same-tree/description/
'''

#Method-1: 
# traverse through each node using bfs or dfs and compare each node in both trees

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        b1, b2 = deque([p]), deque([q])

        while b1 and b2:
            t1 = b1.popleft()
            t2 = b2.popleft()

            if t1.val != t2.val:
                return False
            if t1.left and t2.left:
                b1.append(t1.left)
                b2.append(t2.left)
            elif t1.left or t2.left:
                return False

            if t1.right and t2.right:
                b1.append(t1.right)
                b2.append(t2.right)
            elif t1.right or t2.right:
                return False
            
        return True

#Time: O(n)
#Space: O(n) {O(p) + O(q)}

#-----------------------------------------------------------------------------------------------

#Method-2: Recursive check
'''
If current node is same in both trees, check their corresponding left and right subtrees
3 base cases:
If p and q both are empty: True ==> Either both trees or empty or we reached leaf
If p, q values are not equal: Fasle
If one of p , q is Null and other is not : False ==> Obvious
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )
       
#Time: O(n)
#Spcae: O(n)

#----------------------------------------------------------------------------------------------

#Method-3: Cheeky way 😉

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return str(p) == str(q)
