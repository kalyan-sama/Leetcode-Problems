'''
Difficulty: Medium

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
'''

'''
Approach:
koko can eat atleast 1 banana or atmost max(piles) of bananas in an hour
Brute force way is to iterate from 1 banana to max(piles) bananas and calculate the no of hrs to complete all the piles

Since it is sorted traversal from 1 to max(piles) we can use binary search
At a particular point, if no hrs is greater than reqd hrs, then koko should consume more bananas per hr. So, update the left pointer to mid + 1

If no hrs is less than or equal to reqd hrs, it could be a possible solution. We move towards left of the array and check other possibilities and find the min bananas
'''

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        curr = 1
        last = max(piles)
        ans = last
        while curr<= last:
            count = (curr+last)//2
            hours = 0

            for i in range(len(piles)):
                hours += int(math.ceil(float(piles[i])/count))
            
            if hours > h:
                curr = count + 1

            elif hours <= h:
                last = count - 1
                ans = min(ans, count)
        return ans
  
#Time: O(log(max(piles)) * len(piles))
#Spce: O(1)
