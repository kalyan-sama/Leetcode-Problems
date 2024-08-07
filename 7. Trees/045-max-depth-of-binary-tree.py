'''
Difficulty: Easy

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
'''

#Method-1: using depth-first search

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
#Time: O(n)
#Spce: O(n)

#------------------------------------------------------------------------------------------

#Method-2: Using breadth-first search

'''
Traverse each level of the tree and use a queue to store the nodes.

Initially insert the root node into the queue.
At next level, pop the parent node from the queue, and add its children.
Repeat the same for all the levels. 

Return the depth, when the queue is empty.
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = deque([root])
        level = 0
        while q:
            n = len(q) #snapshot of queue at the beginning of operations
            for i in range(n):
                node = q.popleft() #pop parent from queue
                #add children of popped node to queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return level
    
#Time: O(n)
#Spce: O(n)

#------------------------------------------------------------------------------

#Method-3: Iterative depth First search

'''
we perfrom depth first search iteratively using a stack.
use pre order traversal and store the nodes in the stack

pop a node from the stack, and add its children to the stack and increment the depth. This ensures depth first search
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [[root, 1]] #Initial node
        ans = 0

        while stack:
            node, depth = stack.pop()

            if node:
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
                ans = max(ans, depth)

        return ans
    
#Time: O(n)
#Spce: O(n)
