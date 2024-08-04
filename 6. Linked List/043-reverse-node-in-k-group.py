'''
Difficulty: Hard

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
'''

#Method:
'''
Traverse through the linked list as  group of k nodes.
Reverse the group and update the previous and the next pointers of the group

Inorder to update the previous and the next pointers of the group, we need to track them through variables
For ex: 1 -> 2 -> 3 -> 4, assume we try to reverse the group 2 -> 3
groupPrev = 1 -> and groupNext = -> 4 (next element after kth element)
After revsering the group, groupPrev should point 3(lst element in group or kth element) and 2 should point groupNext 
=>1 -> 3 -> 2 -> 4


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break #Break when reached end of list

            groupNext = kth.next #Next node after group

            #Reverse the group
            #Prev pointer will be last node from previous group
            #curr pointer will be first node from current group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev

                prev = curr
                curr = temp
            
            #After reversing the group, we need to update the pointer of last node(kth node),
            #  and also update the groupPrev node to set to previous node of next group

            # Before reversing(2->3): 1(groupPrev)->2->3(kth)->4 
            # After reversing1: 1(groupPrev)->2<-3(kth)->4 ==> 1->3->2(groupPrev)->4
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next
    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr #Returns None when reached to the end of the list

        