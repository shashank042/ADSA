from typing import Optional

#876. Middle of the Linked List
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
#solution -1
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        mid_ind = count //2
        temp = head
        for i in range(mid_ind):
            temp = temp.next
        return temp
#solution -2

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        
        # Traverse until fast reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
#141. Linked List Cycle
#solution -1
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited =set()
        temp=head
        while temp:
            if temp in visited:
                return True
            visited.add(temp)
            temp= temp.next
        return False
#solution -2   
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       slow ,fast= head,head
       while fast and fast.next:
        fast= fast.next.next
        slow= slow.next
        if slow == fast:
            return True
       return False
#19. Remove Nth Node From End of List
#Soulution -1
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = 0
        temp = head
        while temp:
            count += 1
            temp =temp.next
        dummy = ListNode()
        dummy.next= head
        temp = dummy
        for _ in range(count - n):
            temp =temp.next
        temp.next = temp.next.next
        return dummy.next
#solution -2


#21. Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy
        
        # Traverse both lists and append the smaller node to current
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remaining nodes from list1 or list2
        current.next = list1 if list1 else list2
        
        # Return the head of the merged list (skipping dummy)
        return dummy.next