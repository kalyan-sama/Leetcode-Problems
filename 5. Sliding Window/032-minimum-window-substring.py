'''
Difficulty: Hard

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string
'''

#Method-1: Brute Force using sliding window
'''
Start with window size = len(t)
Check if check if every char in t is present in hash of window. If yes, we found min string. Otherwise move the window by 1 char to right untill the end and check the same

If min string is not found, increase the window size by 1 char and start checking from beginning till end.
Repeat this untill we find reqd string or untill we cannot increase the window size anymore  
'''

import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def isSubstr(k):
            k_map = collections.Counter(k)
            for char in t:
                if k_map[char] < 1:
                    return False
                k_map[char] -= 1
            return True

        window = len(t)
        while window <= len(s):
            l, r = 0, window
            while r <= len(s):
                # k = s[l:r]
                if isSubstr(s[l:r]):
                    return s[l:r]
                l += 1
                r += 1
            window += 1
        return ''
    
#Time: O(s^2 * t)
#Space: O(s)

#Method-2: using dynamic sliding window
'''
For each window, check if required chars in t is matching with the window.
IF not matching, increase the window size. Else decrease the window size by incrementing left pointer.
Find the min length string

Instead of checking both hashmaps every time, we maintain 2 values 'have' and 'need' 
'need' - indicates no of chars required in t.
'have' - indicates no of chars required in s.

Everytime window changes, we update the have value and compare it with 'need'

If both are equal, we found a possible solution. But there could exist a smaller string. so, we decrease the window size and check again
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_map, window = {}, {}
        
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        l, r = 0, 0
        have, need = 0, len(t_map)
        indices, ansLen = [-1, -1], float('inf')
        while r < len(s):
            #Add the character to window
            window[s[r]] = 1 + window.get(s[r], 0)

            #Check if the current char is present in t_map. If yes, update the have value
            if s[r] in t_map and window[s[r]] == t_map[s[r]]:
                have += 1

            #When all required chars are mapped, decrease the window size to get min length string
            #Increment left pointer untill have value is changed. We could find a potential solution

            while have == need:
                #upadate result
                if (r - l + 1) < ansLen:
                    indices = [l, r + 1]
                    ansLen = (r - l + 1)

                #Remove the left most char from the window
                window[s[l]] -= 1

                #Check if this removal altered the have value or not. 
                #IF the removed char is also in t_map, then it will definitely change the have value

                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    have -= 1

                l += 1
            r += 1
        
        ans = s[indices[0] : indices[1]]

        return ans
    
#Time: O(s)
#Space: O(s)
