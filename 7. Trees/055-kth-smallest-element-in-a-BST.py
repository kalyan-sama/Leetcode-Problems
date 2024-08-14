'''
Difficulty: Medium

Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
'''

#Method-1: 
'''
Traverse through every node and create an array
Sort the array and return kth smallest element
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        q = deque([root])
        ans = []

        while q:
            node = q.popleft()
            if node:
                ans.append(node.val)
                q.append(node.left)
                q.append(node.right)
        
        ans.sort()
        return ans[k - 1]

#Time: O(n) + O(nlogn)
#Space: O(n) + O(n)

#------------------------------------------------------------------------------

#Method-2: Recursive dfs using stack

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        self.kth = 0
        def dfs(node, k):
            if not node:
                return None
            
            dfs(node.left, k)
            stack.append(node.val)
            if len(stack) == k: 
                self.kth = stack[-1]
            dfs(node.right, k)
        dfs(root, k)
        return self.kth

#Time: O(n)
#Space: O(n) + O(n)

#------------------------------------------------------------------------------

#Method-2.2: without using stack

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.kth = None

        def dfs(node, k):
            if not node:
                return None
            
            dfs(node.left, k)
            self.count += 1

            if self.count == k:
                self.kth = node
                return
            dfs(node.right, k)
        dfs(root, k)
        return self.kth.val

#Time: O(n)
#Space: O(n)


#------------------------------------------------------------------------------

#Method-3:Iterative approach

'''
Following inorder traversal we go to the left most node in the tree and insert every node in the way into stack

When we reach NULL, we pop node from stack
Since we pop one element, we visited one element, increment the count
Now, we add the right node of the current popped node to the stack.

Repeat this until k nodes are popped/visited
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cur = root
        stack = []
        count = 0
        while cur or stack:
            while cur: 
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            count += 1

            if count == k:
                return cur.val
            cur = cur.right
        
#Time: O(n)
#Space: O(n)
