'''
Difficulty: Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

#Method-1: Brute force
'''
For each window, compute the max value and append to ans
'''

import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l, r = 0, k
        ans = []
        wmax = float('-inf')

        while r <= len(nums):
            wmax = max(nums[l:r])
            ans.append(wmax)
            l += 1
            r += 1
        
        return ans
    
#Time: O(n * k)

#----------------------------------------------------------------------

#Method-2: Using queue data structure (monotonically decreasing)
'''
Disadvantage of brute force is that we end up comparing same numbers repeatedly, which is unnecessary. 
To avoid this, we try to preserve the max values.

We can use the queue data structure to store and delete the max values
Push only if the current value is lesser than the right end of queue. 
If it is greater, then pop from right until we get a smaller value

The left most end will be the max value of the current window. 
pop the left most value if the window moves out of its scope
'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l, r = 0, 0
        ans = []
        q = collections.deque() #Store index into queue so that we can easily access corresponding values

        while r < len(nums):
            #before adding to queue, delete values which are less than r in the queue
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            #move the left pointer
            if l > q[0]:
                q.popleft()
            
            #Add max value to ans only when window size is achieved (This would apply only to inital window)
            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l += 1
            r += 1

        return ans

#Time: O(n)
