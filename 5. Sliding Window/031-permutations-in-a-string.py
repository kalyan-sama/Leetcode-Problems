'''
Difficulty: Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''


#Method-1: Brute force using sliding window
'''
Use a sliding window of fixed length = len(s1)
Traverse through the string s2 and check if the sorted version of window matches the s1 or not.
'''

import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        window = len(s1)
        i = 0
        s3 = sorted(list(s1))
        while i < len(s2):
            s4 = sorted(list(s2[i:i+window]))
            if s3 == s4:
                return True
            i += 1
        
        return False
        

#Time: O(n.nlogn) = O(n^2)
#Sapce: O(n)

#---------------------------------------------------------------------------------

#Mtehod-2: Using sliding window algorithm and hashmap 
'''
Create a counter hashmap of s1. 
Use a window of fixed length len(s1) and iterate through s2
Add charaters in window to the counter map of s2. If both counter maps are equal, then we found the s1 in s2.
If not, we move to next character in string by adding a new character right of window, and removing the left character from the left side of the window.
'''

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        i = len(s1) - 1
        s3 = collections.Counter(s1)
        s4 = collections.Counter(s2[:len(s1)]) #Add elements in inital window to the counter map
        while i < len(s2)-1: #Iterate from next character after window size
            if s3 == s4:
                return True
            
            #Move the window
            s4[s2[i+1]] += 1 #Add next character to the counter map
            s4[s2[i-len(s1) + 1]] -= 1 #remove start character of the window from the counter map
            if s4[s2[i-len(s1) + 1]] < 1:
                del s4[s2[i-len(s1) + 1]] 
            i += 1
        
        return s3 ==s4
        
#Time: O(n)
#Sapce: O(n)

#-------------------------------------------------------------------------------------

#Method-2.1: Different way to do the 2nd method
#Instead of adding the 1st window to the counter map, we start from 0th index

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        i = 0
        s3 = collections.Counter(s1)
        s4 = collections.Counter()
        while i < len(s2):
            s4[s2[i]] += 1
            if i >= len(s1):
                if s4[s2[i-len(s1)]] > 1:
                    s4[s2[i-len(s1)]] -= 1
                else:
                    del s4[s2[i-len(s1)]] 
            i += 1
            if s3 == s4:
                return True
        
        return s3 ==s4
        
#Time: O(n)
#Sapce: O(n)
