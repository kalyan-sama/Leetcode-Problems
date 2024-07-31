'''
Difficulty: Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

https://leetcode.com/problems/reverse-linked-list/description/
'''

#Method-1: Creat a new linked list with reversed elements
'''
Create a new linked list by inserting each node at the head
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        new_head = None
        curr = head

        while curr is not None:
            node = ListNode(curr.val)

            node.next = new_head
            new_head = node

            curr = curr.next
        
        return new_head
    

#Time: O(n)
#Space: O(n)

#------------------------------------------------------------------------------

#Method-2: update the linked list pointers in palce
'''
Traverse the linked list and update the pointers to point previos node

Initialize 2 pointers prev  = null and curr = head
Traverse each node and exchange the prev, curr pointers
Move both pointers one step forward
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head

        while curr is not None:
            nxt_pointer = curr.next #Store teh next node
            curr.next = prev        #Reverse the link

            prev = curr             #Move prev one step forward
            curr = nxt_pointer      #Move curr one step forward

        return prev
        
#Time: O(n)
#Space: O(1)
