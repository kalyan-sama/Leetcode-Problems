'''
Difficulty: Easy

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

#Method-1: using hashmap
'''
Traverse through the linked list and store the next pointers in the hashmap.

If a node pointing to a node which is already in the hashmap, then cycle exists.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nextPtr = {}
        curr = head
        while curr:
            if curr.next and curr.next in nextPtr:
                return True
            nextPtr[curr.next] = curr
            curr = curr.next
        return False
        
#Time: O(n)
#Space: O(n)

#--------------------------------------------------------------------------------

#Method-2: slow-fast approach (linear space)
'''
Use the slow-fast approach and traverse the list.

If at any point, the slow and fast pointers meet, then cycle exists. (floyd tortoise and hare algorithm)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                
        return False
        
#Time: O(n)
#Space: O(1)
