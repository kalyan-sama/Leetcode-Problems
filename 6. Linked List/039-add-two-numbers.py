'''
Difficulty: Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

#Method-1: Convert list to number
'''
Convert both lists to numbers and add them to get result.
Convert the result to linked list
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = 0, 0
        d1, d2 = 1, 1
        while l1:
            num1 += d1 * l1.val
            d1 *=10
            l1 = l1.next

        while l2:
            num2 += d2 * l2.val
            d2 *= 10
            l2= l2.next
        
        ans = num1 + num2

        print(ans)
        dummy = ListNode(0)
        tail = dummy

        while ans > 0:
            val = ans % 10
            ans //= 10
            node = ListNode(val)
            tail.next = node
            tail = tail.next

        if dummy.next:
            return dummy.next
        return dummy
    
#Time: O(n)
#Space: O(n)

#-------------------------------------------------------------------------------
    
#Method-2: Direct approach
'''
Add 2 node values and carry value from previous addition. Create new node from this value. 
If sum is 2 digit number, carry value to next node.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            tail.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tail = tail.next

        if dummy.next:
            return dummy.next
        return dummy
    
#Time: O(n)
#Space: O(n)
