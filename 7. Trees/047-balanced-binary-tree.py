'''
Difficulty: Easy

Given a binary tree, determine if it is height-balanced
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

https://leetcode.com/problems/balanced-binary-tree/description/
'''

#Method-1: 
'''
Traverse each node in BFS order and compute the max height of both left and right subtrees
If the diffrence is greater than 1 then the tree is not height-balanced tree
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #Helper function to compute the max height of treee from the given node using DFS
        def maxDepth(node):
            ans = 0
            stack = [[node, 1]]
            while stack:
                node, depth = stack.pop()
                if node:
                    stack.append([node.left, depth + 1])
                    stack.append([node.right, depth + 1])
                    ans = max(ans, depth)
            return ans

        #Use queue to store the traversed nodes in BFS order
        q = deque([root])

        while q:
            curr = q.popleft()
            #Compute max left and max right heights of the current node
            leftDepth, rightDepth = 0, 0
            if curr and curr.left:
                q.append(curr.left)
                leftDepth = maxDepth(curr.left)

            if curr and curr.right:
                q.append(curr.right)
                rightDepth = maxDepth(curr.right)
            
            if abs(leftDepth - rightDepth) > 1:
                return False
        return True
        
#Time: O(n^2)  {O(n) for visiting each node and O(n) for computing the max height of each node}
#Space: O(n) 

#----------------------------------------------------------------------------------------------------------------------

#Method-2:
'''
In method-1, we compute the max height of left and right subtrees. So, we are visiting the same nodes multiple times.
To avoid this, we need to somehow return the max height of each node to its parent node.
For this, we need to do backtracking from the leaf node and return the height to its parent node
By this way, we only visit each node atmost once
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node): #returns [isbalanced, depth]
            if not node:
                return [True, 0]
            
            #recursively call the dfs function on the left and right nodes
            left, right = dfs(node.left), dfs(node.right)

            #Check if the current subtree is balanced or not
            # For it to be balanced, its left and right subtrees must be balanced and their difference must be <= 1 
            isbalanced = (
                left[0] and right[0] and
                abs(left[1] - right[1]) <= 1
            )

            return [isbalanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

#Time: O(n) 
#Space: O(n)
