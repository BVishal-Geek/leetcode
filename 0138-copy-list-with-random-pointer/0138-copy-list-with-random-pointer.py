# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hold_data = {}
        curr = head

        if not head:
            return None

        while curr: 
            hold_data[curr] = Node(curr.val)
            curr = curr.next
        
        for original, new in hold_data.items():
            nxt = hold_data.get(original.next)
            random = hold_data.get(original.random)

            new.next = nxt 
            new.random = random
        
        return hold_data[head]
        