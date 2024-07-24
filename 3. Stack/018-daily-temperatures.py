'''
Difficulty: Medium

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''

#Method-1: Brute force
#Loop through every temperature and count the number of days where the temperature is higher

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(temperatures)
        for i in range(n -1):
            days = 0
            for j in range(i + 1, n):
                days +=1
                if temperatures[i] < temperatures[j]:
                    break
                elif j == n - 1:
                    days = 0
                    break
                    
            ans.append(days)
        ans.append(0)
        return ans
    
#Time: O(n^2)
#Space: O(n)

#----------------------------------------------------------------

#Method-2: Using stack
#use stack to store (temperature, index) pairs
#If next temp is higher than top, pop the top and find the difference b/w index values
#else push the pair to stack

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                s_temp, s_index = stack.pop()
                ans[s_index] = (i - s_index)
            stack.append((t, i))

        return ans

#Time: O(n)
#Space: O(n)
