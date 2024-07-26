'''
Difficulty: Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

#Method-1: Iterative

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0 , len(nums) - 1
        if len(nums) == 1 and nums[0] == target:
            return 0 
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        return -1
    
#Time: O(logn)
#Space: O(1)

#----------------------------------------------------------------

#Method-2: Recursive

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0 , len(nums) - 1
        if len(nums) == 1 and nums[0] == target:
            return 0 
        def recursive(nums, left, right):
            if left > right:
                return -1
            mid = (left + right) //2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return recursive(nums, mid + 1, right)
            else:
                return recursive(nums, left, mid - 1)

        return recursive(nums, l, r)
    
#Time: O(logn)
#Space: O(1)
