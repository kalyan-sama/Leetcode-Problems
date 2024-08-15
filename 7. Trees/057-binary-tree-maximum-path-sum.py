'''
Difficulty: Hard

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
'''

'''
Approach:


for tree : 2 ==> max path sum is 2
for [1,2,3]
    1
   /  \
  2    3
ans = max(left) + root + max(right)

These 2 will be the base cases for the recutrsion

But, for max path sum, we can only have one split in the entire tree. 
i.e, for only one node, we can traverse both left and right directions.

For the remaining nodes, we should only select the path which gives the maximum sum.

Inorder to find the maximum sum, we find the max sum for all subtrees and update the answer.
And for each node, we will return the max maximum sum of left and right directions
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = root.val

        def dfs(node):
            if not node:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            #Ignore -ve values because they don't contribute to max sum
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #Compute max path sum with split and upadte ans
            self.ans = max(self.ans, leftMax + node.val + rightMax)

            return node.val + max(leftMax, rightMax) #return max path sum without split
        dfs(root)
        return self.ans

#Time: O(n)
#Space: O(h)
