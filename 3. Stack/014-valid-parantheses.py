'''
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

#Method-1: 

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [s[0]]
        for i in range(1, len(s)):
            if self.isEmpty(stack):
                stack.append(s[i])
                continue

            if s[i] in ('(', '{', '['):
                stack.append(s[i])
                continue
            
            if s[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])

            if s[i] == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(s[i])

            if s[i] == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[i])
        
        return stack == []

    def isEmpty(self, stack):
        return stack == []
            
#Time: O(n)
#Space: O(n)

#----------------------------------------------------------------

#Method-2: Using hashmap

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in hashmap:
                if stack and stack[-1] in hashmap[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        
        return not stack
    
#Time: O(n)
#Space: O(n)
