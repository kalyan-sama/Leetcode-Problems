'''
Difficulty: Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
'''

#Method-1: Brute force
#for every height, find the leftmax and rightmax heights
#Trapped water would be b/w leftmax and rightmax with height as min of both excluding curr height

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(height)):
            leftmax, rightmax = 0, 0
            for j in range(0, i):
                leftmax = max(leftmax, height[j])
            
            for j in range(i, len(height)):
                rightmax = max(rightmax, height[j])
            
            ans += max(0, min(leftmax, rightmax) - height[i])

        return ans
        
#Time: O(n^2)
#Space: O(1)

#----------------------------------------------------------------

#Method-2: DP
#Store prefixmax and suffixmax values in seperate arrays

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        prefix_max = [height[0]] * n      
        suffix_max = [height[-1]] * n
        ans = 0
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], height[i])
        
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i])
        
        for i in range(n):
            ans += (min(prefix_max[i], suffix_max[i]) - height[i])
        
        return ans

#Time: O(n)
#Space: O(n)

#----------------------------------------------------------------

#Method-3: without using extra space to store prefix, suffix max values
#Find the max height in the list and split the lsit into 2 halves at the max height

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        mid = 0
        max_height = 0
        ans = 0

        for i in range(n):
            if max_height < height[i]:
                max_height = height[i]
                mid = i
        
        lmax = 0
        for i in range(mid):
            lmax = max(lmax, height[i])
            ans += lmax - height[i]
        
        rmax = 0
        for i in range(n-1, mid, -1):
            rmax = max(rmax, height[i])
            ans += rmax - height[i]

        return ans
        
#Time: O(n)
#Space: O(1)

#----------------------------------------------------------------

#Method-4: 2 pointer

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        ans = 0
        
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                ans += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                ans += rmax - height[r]
        
        return ans

#Time: O(n)
#Space: O(1)
