'''
Difficulty: Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''

#Method-1: sort and count the sequence

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        ans = 1
        t = 1
        for i in range(1, len(nums)):            
            if nums[i] - nums[i - 1] ==1:
                t += 1 
            else:
                t = 1
            if (ans <= t):
                ans = t
        return ans
    
#Time: O(nlogn)
#Space: O(1)

#Method-2: without sorting

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        ans = 0

        for n in nums:
            #check if n is start of the sequence or not
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                ans = max(length, ans)
        return ans 
    
#Time: O(n)
#Space: O(n)