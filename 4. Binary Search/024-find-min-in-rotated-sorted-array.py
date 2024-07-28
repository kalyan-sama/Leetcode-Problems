'''
Difficulty: Medium

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
'''


'''
Approach: Since it is rotated sorted array, there will be 2 sorted sub arrays
We need to determine which sub array will contain the min value

We can use binary search to identify the pivot of 2 arrays.
Compare the mid with either left or right

If mid < right: then, min value will be in left half
if mid > right: then, min value will be in right half

4 5 6 7 8 9 0 1 2 3
l       m         r
m > r => l = m + 1
4 5 6 7 8 9 0 1 2 3
          l   m   r
m < r => r = m
4 5 6 7 8 9 0 1 2 3
          l m r
m < r => r = m
4 5 6 7 8 9 0 1 2 3
          l r
m > r => l = m + 1
4 5 6 7 8 9 0 1 2 3
            lr
r == l => return l

7 8 0 1 2 3 4 5 6
l       m       r
m < r => r = m
7 8 0 1 2 3 4 5 6
l m     m
m > r => l = m + 1
7 8 0 1 2 3 4 5 6
    l m r
m < l => r = m
7 8 0 1 2 3 4 5 6
    l r
m < r => r = m
7 8 0 1 2 3 4 5 6
    lr
r == l => return l

'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) -1 

        while l <= r:            
            mid = (l + r)//2

            if nums[mid] < nums[r]:
                r = mid

            elif nums[mid] > nums[r]:
                l = mid + 1

            if nums[r] == nums[l]:
                return nums[l]
        
#Time: O(logn)
#Space: O(1)