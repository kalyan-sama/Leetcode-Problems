'''
Difficulty: Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
'''

#Method-1: using prefix, postfix arrays

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1 for _ in range(len(nums))]
        postfix = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for j in range(len(nums)-2, -1, -1):
            postfix[j] = postfix[j + 1] * nums[j + 1]

        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * postfix[i])
        
        return ans
        
#Time: O(n)
#Space: O(n)

#----------------------------------------------------------------------

#Method-2: without using new arrays

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        postfix = 1
        ans = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]

        for j in range(len(nums)-1, -1, -1):
            ans[j] = ans[j] * postfix
            postfix *= nums[j]
        
        return ans
    
#Time: O(n)
#Space: O(1)