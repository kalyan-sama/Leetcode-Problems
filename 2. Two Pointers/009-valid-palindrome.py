'''
Difficulty: Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

#Method-1: using new string and inbuilt funcitons

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ""
        for c in s:
            if c.isalnum():
                s1+=c.lower()
        return s1 == s1[::-1]
    
#Time: O(n)     n: length of s
#Space: O(n)

#----------------------------------------------------------------------

#Method-2: 2 pointer approach with const space and without using inbuilt funs

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.check_alpha_num(s[l]):
                l += 1
            while r > l and not self.check_alpha_num(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def check_alpha_num(self, c):
        return(
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )
        

#Time: O(n)
#Space: O(1)
