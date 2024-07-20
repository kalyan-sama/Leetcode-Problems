'''
Difficulty: Easy

Given an integer array nums, return true if any value appears at least twice in the array,
  and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

#Method-1: Brute force
from typing import List

def containsDuplicate(self, nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Time: O(n^2)
# Space: O(1)

#----------------------------------------------------------------------

#Method-2: Sorting

def containsDuplicate(self, nums: List[int]) -> bool:
    sorted_nums = sorted(nums)
    for i in range(1, len(nums)):
        if sorted_nums[i] == sorted_nums[i-1]:
            return True
    return False

# Time: O(nlogn)
# Space: O(1)

#----------------------------------------------------------------------

#Method-3: Using hash set

def containsDuplicate(self, nums: List[int]) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

# Time: O(n)
# Space: O(n)