'''
Difficulty: Easy

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 
'''

'''
We use DFS to identify the max depth of left and right subtrees and add them to get the max diameter
But the max depth may or may not pass through root node. 

So, we find the max diameter of each node in the tree by recursively running dfs, and return the maximum depth
At each step, we identify the max height of left and right subtrees and the diameter would be left + right
We return the maximum height of left and right nodes to their parent node
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(node):
            # Base case: if the node is None, return 0
            if not node:
                return 0

            # Recursively calculate the height of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Update the maximum diameter encountered so far
            self.ans = max(self.ans, left + right)

            # Return the height of the current node to the caller(its parent)
            return 1 + max(left, right)
        
        dfs(root)
        return self.ans

#Time: O(n)
#Space: O(n)
