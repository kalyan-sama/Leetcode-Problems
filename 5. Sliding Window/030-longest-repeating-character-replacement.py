'''
Difficulty: Medium

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''

#Method-1: 
'''
use sliding window starting from 0
for the substring in window, find the maximum repeated letter count. 
This can be done by storing the chars in substring in hashmap and returning the max count

Idea is to keep the max repeated char and replace the remaining letters. This will allow us to find the required string in minimum steps
Since we want all letters in substring to be same, we should check if remaining letters are less than or equal to k operations
If yes, we can replace all chars and get a possibility of required substring. Inc right pointer to check remaining string
If not, we should decrease the size of the window by increasing left pointer
'''

import collections

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #Function to return max repated character count 
        def maxFreq(substring):
            hashmap = collections.Counter(substring)
            maxf = 0
            for s in hashmap:
                maxf = max(maxf, hashmap[s])
            return maxf
        
        l, r = 0, 0
        ans = 0

        while r < len(s):
            if len(s[l:r+1]) - maxFreq(s[l:r+1]) <= k:
                ans = max(ans, r - l + 1)
            else:
                l += 1
            r += 1
        
        return ans
    
#Time: O(26 * n) #since for every cnew character, we are checking the max freq in hashmap. In worst case it will take O(26)
#Space: O(n)

#--------------------------------------------------------------------------------------------------------------------------------

#Method-2: improve the above function

'''
Instead of calling the same function for evry substring, we can maintain a hashmap where we can add/upadte characters when window size changes
'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hashmap = {}
        l, r = 0, 0
        ans = 0

        while r < len(s):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0) 
            if len(s[l:r+1]) - max(hashmap.values()) <= k:
                ans = max(ans, r - l + 1)
            else:
                hashmap[s[l]] -= 1
                l += 1
            r += 1
        
        return ans
    
#Time: O(26 * n) = O(n)
#Space: O(n)

#Method-3: improve method-2
'''
small disadvantage of method-2 is that every time we compute the max value by iterating over the entire hashmap.
Instead of doing that, we can memorize the max value and update it whenever new value is inserted into the hashmap

By doing this, we can reduce the O(26) time
'''

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hashmap = {}
        l, r = 0, 0
        ans = 0
        maxf = 0 #To memorize the max value
        while r < len(s):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxf = max(maxf, hashmap[s[r]]) #whenever an element is changed in hashmap, update the maxf value
            if len(s[l:r+1]) - maxf <= k:
                ans = max(ans, r - l + 1)
            else:
                hashmap[s[l]] -= 1
                l += 1
            r += 1
        
        return ans
    
#Time: O(n)
#Space: O(n)
