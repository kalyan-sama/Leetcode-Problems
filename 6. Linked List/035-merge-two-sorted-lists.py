'''
Difficulty: Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

1->2->4
1->3->4

1->2->3->4->4

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

'''

'''
Create a dummy node at the beginning of the list and add a tail pointer to it
Traverse through both the lists.

When smallest node is found, update the tail pointer to point to the smallest node. Move the tail pointer to the next node
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1, l2 = list1, list2
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1    # update the tail pointer to point to the next node
                l1 = l1.next      # move the l1 pointer
            
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next      # move the tail pointer to the next node

        #If there are any nodes left in l1 or l2, then add them to the list
        #Since the list is sorted, we can just update the tail pointer to point to the 1st node of remaining list
        if l1:
            tail.next = l1

        if l2:
            tail.next = l2
        
        return dummy.next #Return head without dummy node

#Time: O(n + m)
#Space: O(1)
