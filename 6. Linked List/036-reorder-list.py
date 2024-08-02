'''
Difficulty: Medium

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 
https://leetcode.com/problems/reorder-list/description/
'''

#Method-1:
'''
Convert linked list into list
Split the list into 2 halves. Reverse the 2nd half
Merge both lists with value from first half follwed by value from second half
Replace the node values in linked list with value from merged list
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next
        if len(l)%2 == 0:
            mid = len(l)//2
        else:
            mid = len(l)//2 + 1
        
        merged = []
        left, right = l[:mid], l[mid:]
        right = right[::-1]
        for i in range(len(right)):
            merged.append(left[i])
            merged.append(right[i])
        if len(l) % 2 != 0 and len(merged) > 1:
            merged.append(left[-1])
        
        print(merged)
        curr = head
        for i in merged:
            curr.val = i
            curr = curr.next
        
#Time: O(n)
#Space: O(n)

#----------------------------------------------------------------------------------

#Method-2: Without using additional space. Update the pointers in place

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #find the mid point

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # mid = slow => 1st node of 2nd half is slow.next

        second_head = slow.next
        prev = None

        slow.next = None # Remove the pointer of last node in the 1st half

        while second_head:
            temp = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = temp

        #After reversing the send half, second_head will point to null and prev will point to beginning of send half

        first, second = head, prev

        #Since 2nd half is always smaller than first, we start with second head
        while second:
            #Store the next pointers in both lists and use them to move to the next nodes
            temp1 = first.next
            temp2 = second.next

            #update the pointer in first list to point to second. Move head of first list
            first.next = second
            first = temp1
            
            #update the pointer in second list to point to first. Move head of second list
            second.next = first
            second = temp2

#Time: O(n)
#Space: O(1)
