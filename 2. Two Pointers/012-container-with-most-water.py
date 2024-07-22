'''
Difficulty: Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
'''

#Method-1: Brute force

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = ((j + 1) - (i + 1)) * min(height[j], height[i])
                ans = max(ans, area)
        return ans
    
#Time: O(n^2)
#Space: O(1)

#----------------------------------------------------------------

#Method-2: 2 pointer

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = ((r + 1) - (l + 1)) * min(height[l], height[r])
            ans = max(area, ans)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
    
#Time: O(n)
#Space: O(1)
