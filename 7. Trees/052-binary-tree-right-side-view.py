'''
Difficulty: Medium

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

https://leetcode.com/problems/binary-tree-right-side-view/description/
'''

#Method-1:
'''
Using BFS, traverse through the tree and track the last node in the current level
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        curr = root
        ans = []
        q = deque([root])

        while q:
            rightNode = -111
            currLen = len(q)
            for _ in range(currLen):
                node = q.popleft()
                if node:
                    rightNode = node.val
                    q.append(node.left)
                    q.append(node.right)
                
            if rightNode != -111:
                ans.append(rightNode)
        return ans

#Time: O(n)
#Space: O(n)
