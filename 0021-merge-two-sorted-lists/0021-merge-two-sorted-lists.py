# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy

        # if not list1 and not list2:
        #     return None
        
        # if (not list1 and list2.val == 0) or (not list2 and list1.val == 0):
        #     return [0]
    
        while list1 and list2: 
            if list1.val <= list2.val: 
                tail.next = list1
                list1 = list1.next

            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2 
        return dummy.next