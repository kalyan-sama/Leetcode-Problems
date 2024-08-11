'''
Difficulty: Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

https://leetcode.com/problems/binary-tree-level-order-traversal/description/
'''

#Method-1:
'''
Use BFS to traverse through each node in the tree and assign a level value to each node.
Add the node to the list according to its level value. 
'''
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans =[]
        if root:
            q = deque([(root, 0)])  # [(node, level)]
            ans.append([root.val]) 
        else:
            return []
        while q:
            node, level = q.popleft()
            if node.left:
                ind = level + 1
                if len(ans) > ind:
                    ans[ind].append(node.left.val) #If the list for the current level already exists, add the node to the list
                else:
                    ans.append([node.left.val]) # else, create a new list for the new level
                q.append((node.left, ind))
            if node.right:
                ind = level + 1
                if len(ans) > ind:
                    ans[ind].append(node.right.val)
                else:
                    ans.append([node.right.val])
                q.append((node.right, ind))
        return ans

#Time: O(n)
#Space: O(n)

#---------------------------------------------------------------------------------------------------------------------------------------------

#Method-2:
'''
Instead of tracking every node with it's level number, we pop all the nodes at each level from the queue and add to the list
It can be achieved by using the lenght of the queue at each iteration as it will represent the no of nodes at each level
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans =[]
        q = deque([root]) 
        while q:
            currLen = len(q) # Indicates the number of nodes at each level
            level = []
            #Pop every node at the current level and add it to the list
            #Add the children of all the popped nodes
            for _ in range(currLen): 
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                ans.append(level)

        return ans

#Time: O(n)
#Space: O(n)
