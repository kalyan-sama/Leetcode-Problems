'''
Doifficulty: Hard

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
'''

#Method-1: Brute force
#For each bar, calculate how many bars on the left and right are taller than it.
# area = H(L + R) 
# find max of all areas

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        n = len(heights)

        for i in range(n):
            l, r = 0, 0
            for j in range(i, -1, -1):
                if heights[j] < heights[i]:
                    break
                l += 1
            
            for k in range(i, n):
                if heights[k] < heights[i]:
                    break
                r += 1
            area = heights[i] * (l + r - 1) # -1 because, current height will be considered 2 times in l, r
            ans = max(ans, area)

        return ans
    
#Time: O(n^2)
#Space: O(1)

#----------------------------------------------------------------

#Method-2: using stack to store the [index, height] pairs and compute the area

# if top height is greater than next element, then the height cannot be extended further. So it should be popped

#When pushing next height to stack, check if it can be extended backwards. Update the start_index of the new element.
#Since we push the element only if the height is less than previous height, we can always extend the height untill last popped height
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        stack = [] # pair: [start_index, height]
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                ans = max(ans, area)
                start = index
            stack.append([start, h])

        #After processing all the heights in the list, we will end up with few elements in the stack.
        #Compute area for remaining each element in stack

        for pair in stack:
            index, height = pair[0], pair[1]
            area = height * (len(heights) - index)
            ans = max(ans, area)

        return ans