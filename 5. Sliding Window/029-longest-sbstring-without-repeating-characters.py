'''
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

#Method-1: 2-pointer 
'''
Approach:
start both pointers from 0 and move the right pointer forward
if length of the substring is equal to len of set of characters, then we found a substring without repeating characters
if not, then move the left pointer forward
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        ans = 0

        while r <= len(s) :
            if len(s[l:r]) == len(set(s[l:r])):
                ans = max(ans, len(s[l:r]))
            else:
                l += 1
            r += 1
        return ans
    
#Time: O(n)
#Space: O(n)

#---------------------------------------------------------------------------------------------------

#Method-2: Sliding window
'''
Approach:
use dynamic sliding window to expand when new char is identified in sequence and shrink when same char is identified

use hashset to store the current characters in the substring
if the next character is not in hashset, we expand the window by moving right pointer
if the next character is already in hashset, remove the left character from the set until the duplicate is removed.  Decrease the window size by moving left poitner to 1 unit
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        ans = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            ans = max(ans, r - l + 1)
        return ans

#Time: O(n)
#Space: O(n)